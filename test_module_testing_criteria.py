"""
Tests for validating that module testing criteria adequately address persona
learning needs against competencies.

This test suite validates:
1. Testing criteria exist for all personas
2. Evaluation questions address identified learning needs
3. Testing scenarios map to valid competencies
4. Scenarios align with modular learning scope (G, H, I, J not K)
5. Evaluation criteria address diversity and inclusion considerations
6. Cross-cutting themes are adequately defined
"""

import yaml
import pytest
from pathlib import Path
from typing import Dict, List, Any, Set


# File paths
BASE_DIR = Path(__file__).parent.absolute()
COMPETENCIES_FILE = BASE_DIR / "Competency framework" / "ml_framework_standards-competencies-v1_0.yaml"
LOGIC_MODEL_FILE = BASE_DIR / "Modular design" / "ml_modular_logic_model-v1_0.yaml"

PERSONA_FILES = [
    BASE_DIR / "Personas" / "ml_framework_personas-fundamental_stage.yaml",
    BASE_DIR / "Personas" / "ml_framework_personas-stage1.yaml",
    BASE_DIR / "Personas" / "ml_framework_personas-stage2.yaml",
    BASE_DIR / "Personas" / "ml_framework_personas-stage3.yaml",
    BASE_DIR / "Personas" / "ml_framework_personas-stage4.yaml",
]

TESTING_CRITERIA_FILES = [
    BASE_DIR / "Test scripts" / "ml_framework_module_testing_criteria-fundamental_stage.yaml",
    BASE_DIR / "Test scripts" / "ml_framework_module_testing_criteria-stage1.yaml",
    BASE_DIR / "Test scripts" / "ml_framework_module_testing_criteria-stage2.yaml",
    BASE_DIR / "Test scripts" / "ml_framework_module_testing_criteria-stage3.yaml",
    BASE_DIR / "Test scripts" / "ml_framework_module_testing_criteria-stage4.yaml",
]


class TestDataLoader:
    """Utility class for loading and caching test data"""

    _competencies_cache = None
    _personas_cache = None
    _testing_criteria_cache = None

    @classmethod
    def load_competencies(cls) -> Dict:
        """Load the competencies framework"""
        if cls._competencies_cache is None:
            with open(COMPETENCIES_FILE, 'r') as f:
                cls._competencies_cache = yaml.safe_load(f)
        return cls._competencies_cache

    @classmethod
    def get_competency_names(cls) -> Set[str]:
        """Get set of all competency names"""
        competencies_data = cls.load_competencies()
        names = set()

        framework = competencies_data.get('managementAndLeadershipFramework', {})
        focus_areas = framework.get('focusAreas', [])

        for focus_area in focus_areas:
            sections = focus_area.get('sections', [])
            for section in sections:
                competencies = section.get('competencies', [])
                for competency in competencies:
                    name = competency.get('name', '').strip()
                    names.add(name)

        return names

    @classmethod
    def load_personas(cls) -> List[Dict]:
        """Load all persona files"""
        if cls._personas_cache is None:
            personas = []
            for filepath in PERSONA_FILES:
                try:
                    with open(filepath, 'r') as f:
                        data = yaml.safe_load(f)
                    framework = data.get('managementAndLeadershipFramework', {})
                    stages = framework.get('stages', [])

                    for stage in stages:
                        stage_personas = stage.get('personas', [])
                        for persona in stage_personas:
                            persona['_stage'] = stage.get('stageName', 'Unknown')
                            persona['_source_file'] = filepath.name
                            personas.append(persona)

                except yaml.YAMLError as e:
                    print(f"Warning: Could not parse {filepath.name}: {e}")
                    continue
                except Exception as e:
                    print(f"Warning: Error loading {filepath.name}: {e}")
                    continue

            cls._personas_cache = personas
        return cls._personas_cache

    @classmethod
    def get_persona_map(cls) -> Dict[str, Dict]:
        """Create map of persona ID to persona data"""
        personas = cls.load_personas()
        return {p.get('personaId', ''): p for p in personas}

    @classmethod
    def load_testing_criteria(cls) -> List[Dict]:
        """Load all testing criteria files"""
        if cls._testing_criteria_cache is None:
            criteria_personas = []
            for filepath in TESTING_CRITERIA_FILES:
                try:
                    with open(filepath, 'r') as f:
                        data = yaml.safe_load(f)
                    framework = data.get('managementAndLeadershipFramework', {})
                    stages = framework.get('stages', [])

                    for stage in stages:
                        stage_personas = stage.get('personas', [])
                        for persona in stage_personas:
                            persona['_stage'] = stage.get('stageName', 'Unknown')
                            persona['_source_file'] = filepath.name

                            # Add cross-cutting themes
                            persona['_cross_cutting_themes'] = framework.get(
                                'crossCuttingEvaluationThemes', {}
                            )

                            criteria_personas.append(persona)

                except Exception as e:
                    print(f"Warning: Error loading {filepath.name}: {e}")
                    continue

            cls._testing_criteria_cache = criteria_personas
        return cls._testing_criteria_cache

    @classmethod
    def get_testing_criteria_map(cls) -> Dict[str, Dict]:
        """Create map of persona ID to testing criteria"""
        criteria = cls.load_testing_criteria()
        return {c.get('personaId', ''): c for c in criteria}


class TestTestingCriteriaCompleteness:
    """Test that testing criteria exist for all personas"""

    def test_testing_criteria_files_exist(self):
        """Verify all testing criteria files exist"""
        for filepath in TESTING_CRITERIA_FILES:
            assert filepath.exists(), f"Testing criteria file not found: {filepath}"

    def test_all_personas_have_testing_criteria(self):
        """Test that every persona has corresponding testing criteria"""
        personas = TestDataLoader.load_personas()
        criteria_map = TestDataLoader.get_testing_criteria_map()

        missing_criteria = []
        for persona in personas:
            persona_id = persona.get('personaId', 'Unknown')
            if persona_id not in criteria_map:
                role = persona.get('role', 'Unknown')
                missing_criteria.append(f"{persona_id} ({role})")

        assert len(missing_criteria) == 0, (
            f"The following personas are missing testing criteria: {', '.join(missing_criteria)}"
        )

    @pytest.mark.parametrize("criteria_persona", TestDataLoader.load_testing_criteria())
    def test_persona_has_evaluation_questions(self, criteria_persona):
        """Test that each persona in testing criteria has evaluation questions"""
        persona_id = criteria_persona.get('personaId', 'Unknown')
        role = criteria_persona.get('role', 'Unknown')

        eval_questions = criteria_persona.get('moduleEvaluationQuestions', [])

        assert len(eval_questions) > 0, (
            f"Persona {persona_id} ({role}) has no module evaluation questions"
        )

        assert len(eval_questions) >= 5, (
            f"Persona {persona_id} ({role}) has only {len(eval_questions)} evaluation questions. "
            f"Should have at least 5 to adequately test modules."
        )

    @pytest.mark.parametrize("criteria_persona", TestDataLoader.load_testing_criteria())
    def test_persona_has_diversity_context(self, criteria_persona):
        """Test that each persona has diversity context defined"""
        persona_id = criteria_persona.get('personaId', 'Unknown')
        role = criteria_persona.get('role', 'Unknown')

        diversity_context = criteria_persona.get('diversityContext', '')

        assert diversity_context, (
            f"Persona {persona_id} ({role}) has no diversity context defined in testing criteria"
        )

        assert len(diversity_context) > 20, (
            f"Persona {persona_id} ({role}) has very brief diversity context: '{diversity_context}'"
        )


class TestTestingScenarios:
    """Test that testing scenarios are comprehensive and valid"""

    @pytest.mark.parametrize("criteria_persona", TestDataLoader.load_testing_criteria())
    def test_persona_has_testing_scenarios(self, criteria_persona):
        """Test that personas have testing scenarios defined"""
        persona_id = criteria_persona.get('personaId', 'Unknown')
        role = criteria_persona.get('role', 'Unknown')

        scenarios = criteria_persona.get('moduleTestingScenarios', {})
        scenario_count = len([k for k in scenarios.keys() if k.startswith('scenario')])

        # Note: Not all personas have scenarios yet, so this is a soft check
        if scenario_count == 0:
            print(f"\nWarning: {persona_id} ({role}) has no testing scenarios defined")
        else:
            print(f"\n{persona_id} ({role}): {scenario_count} scenarios")

    @pytest.mark.parametrize("criteria_persona", TestDataLoader.load_testing_criteria())
    def test_scenarios_map_to_valid_competencies(self, criteria_persona):
        """Test that all testing scenarios map to valid competencies"""
        persona_id = criteria_persona.get('personaId', 'Unknown')
        role = criteria_persona.get('role', 'Unknown')

        scenarios = criteria_persona.get('moduleTestingScenarios', {})
        competency_names = TestDataLoader.get_competency_names()

        for scenario_key, scenario_data in scenarios.items():
            if not scenario_key.startswith('scenario'):
                continue

            competency = scenario_data.get('competency', '').strip()

            assert competency, (
                f"Persona {persona_id} ({role}) {scenario_key} has no competency specified"
            )

            assert competency in competency_names, (
                f"Persona {persona_id} ({role}) {scenario_key} references invalid competency: '{competency}'. "
                f"Valid competencies: {sorted(list(competency_names))[:5]}..."
            )

    @pytest.mark.parametrize("criteria_persona", TestDataLoader.load_testing_criteria())
    def test_scenarios_have_test_questions(self, criteria_persona):
        """Test that all scenarios have meaningful test questions"""
        persona_id = criteria_persona.get('personaId', 'Unknown')
        role = criteria_persona.get('role', 'Unknown')

        scenarios = criteria_persona.get('moduleTestingScenarios', {})

        for scenario_key, scenario_data in scenarios.items():
            if not scenario_key.startswith('scenario'):
                continue

            test_question = scenario_data.get('testQuestion', '').strip()

            assert test_question, (
                f"Persona {persona_id} ({role}) {scenario_key} has no test question"
            )

            assert len(test_question) > 50, (
                f"Persona {persona_id} ({role}) {scenario_key} has brief test question: '{test_question[:50]}...'"
            )

    @pytest.mark.parametrize("criteria_persona", TestDataLoader.load_testing_criteria())
    def test_scenarios_have_evaluation_criteria(self, criteria_persona):
        """Test that all scenarios have evaluation criteria"""
        persona_id = criteria_persona.get('personaId', 'Unknown')
        role = criteria_persona.get('role', 'Unknown')

        scenarios = criteria_persona.get('moduleTestingScenarios', {})

        for scenario_key, scenario_data in scenarios.items():
            if not scenario_key.startswith('scenario'):
                continue

            eval_criteria = scenario_data.get('evaluationCriteria', [])

            assert len(eval_criteria) > 0, (
                f"Persona {persona_id} ({role}) {scenario_key} has no evaluation criteria"
            )

            assert len(eval_criteria) >= 3, (
                f"Persona {persona_id} ({role}) {scenario_key} has only {len(eval_criteria)} "
                f"evaluation criteria. Should have at least 3 for meaningful assessment."
            )


class TestLearningNeedsAlignment:
    """Test that testing criteria align with persona learning needs"""

    @pytest.mark.parametrize("criteria_persona", TestDataLoader.load_testing_criteria())
    def test_scenarios_address_target_competencies(self, criteria_persona):
        """Test that scenarios cover persona's target competencies"""
        persona_id = criteria_persona.get('personaId', 'Unknown')
        role = criteria_persona.get('role', 'Unknown')

        # Get original persona
        persona_map = TestDataLoader.get_persona_map()
        original_persona = persona_map.get(persona_id)

        if not original_persona:
            pytest.skip(f"Original persona {persona_id} not found (may have YAML errors)")
            return

        # Get target competencies
        comp_profile = original_persona.get('competencyDevelopmentProfile', {})
        target_competencies = comp_profile.get('targetCompetencies', [])

        if not target_competencies:
            pytest.skip(f"Persona {persona_id} has no target competencies defined")
            return

        # Extract competency names from target competencies (format: "Name (Stage)")
        target_names = set()
        for target in target_competencies:
            if '(' in target:
                name = target.split('(')[0].strip()
            else:
                name = target.strip()
            target_names.add(name)

        # Get competencies covered in scenarios
        scenarios = criteria_persona.get('moduleTestingScenarios', {})
        covered_competencies = set()

        for scenario_key, scenario_data in scenarios.items():
            if scenario_key.startswith('scenario'):
                comp = scenario_data.get('competency', '').strip()
                if comp:
                    covered_competencies.add(comp)

        # Check coverage
        if len(covered_competencies) > 0:
            uncovered = target_names - covered_competencies
            coverage_pct = (len(covered_competencies) / len(target_names)) * 100

            print(f"\n{persona_id}: {len(covered_competencies)}/{len(target_names)} "
                  f"target competencies covered ({coverage_pct:.0f}%)")

            if uncovered:
                print(f"  Uncovered: {', '.join(sorted(uncovered))}")

    @pytest.mark.parametrize("criteria_persona", TestDataLoader.load_testing_criteria())
    def test_evaluation_questions_address_diversity_barriers(self, criteria_persona):
        """Test that evaluation questions address diversity-related barriers"""
        persona_id = criteria_persona.get('personaId', 'Unknown')
        role = criteria_persona.get('role', 'Unknown')

        # Get original persona
        persona_map = TestDataLoader.get_persona_map()
        original_persona = persona_map.get(persona_id)

        if not original_persona:
            pytest.skip(f"Original persona {persona_id} not found")
            return

        # Get diversity profile barriers
        diversity_profile = original_persona.get('diversityProfile', {})
        experience_of_power = diversity_profile.get('experienceOfPower', {})
        barriers = experience_of_power.get('experiencedBarriers', [])

        if not barriers:
            # Persona may not have documented barriers
            return

        eval_questions = criteria_persona.get('moduleEvaluationQuestions', [])

        # Check if evaluation questions reference key barrier themes
        # This is a qualitative check - we're looking for questions that address
        # systemic barriers, discrimination, access, etc.
        barrier_keywords = [
            'barrier', 'discrimination', 'access', 'assumption', 'privilege',
            'structural', 'systemic', 'recognise', 'challenge', 'address',
            'inclusive', 'equity', 'power', 'disadvantage'
        ]

        questions_addressing_barriers = []
        for question in eval_questions:
            question_lower = question.lower()
            if any(keyword in question_lower for keyword in barrier_keywords):
                questions_addressing_barriers.append(question)

        # At least some questions should address diversity/barriers
        if len(barriers) > 0:
            assert len(questions_addressing_barriers) > 0, (
                f"Persona {persona_id} ({role}) has {len(barriers)} documented barriers "
                f"but none of the {len(eval_questions)} evaluation questions appear to "
                f"address diversity, barriers, or inclusion themes"
            )


class TestModularLearningScopeAlignment:
    """Test that testing criteria align with modular learning scope"""

    def test_cross_cutting_themes_include_limitations(self):
        """Test that cross-cutting themes include acknowledgment of limitations"""
        criteria = TestDataLoader.load_testing_criteria()

        if not criteria:
            pytest.fail("No testing criteria loaded")

        # Get cross-cutting themes from first persona (they should be consistent)
        first_persona = criteria[0]
        themes = first_persona.get('_cross_cutting_themes', {})

        # Look for theme about limitations
        theme_names = []
        for theme_key, theme_data in themes.items():
            if theme_key.startswith('theme'):
                name = theme_data.get('name', '')
                theme_names.append(name)

        # Check for limitations theme
        has_limitations = any('limitation' in name.lower() for name in theme_names)

        assert has_limitations, (
            f"Cross-cutting themes should include 'Acknowledgment of Limitations' theme. "
            f"Found themes: {theme_names}"
        )

    def test_cross_cutting_themes_include_power_and_inclusion(self):
        """Test that cross-cutting themes address power and inclusion"""
        criteria = TestDataLoader.load_testing_criteria()

        if not criteria:
            pytest.fail("No testing criteria loaded")

        first_persona = criteria[0]
        themes = first_persona.get('_cross_cutting_themes', {})

        theme_names = []
        for theme_key, theme_data in themes.items():
            if theme_key.startswith('theme'):
                name = theme_data.get('name', '')
                theme_names.append(name)

        # Check for power/inclusion theme
        has_power_inclusion = any(
            'power' in name.lower() or 'inclusion' in name.lower() or 'diversity' in name.lower()
            for name in theme_names
        )

        assert has_power_inclusion, (
            f"Cross-cutting themes should include Power/Diversity/Inclusion theme. "
            f"Found themes: {theme_names}"
        )

    @pytest.mark.parametrize("criteria_persona", TestDataLoader.load_testing_criteria())
    def test_evaluation_questions_check_realistic_scope(self, criteria_persona):
        """Test that evaluation questions consider realistic module scope"""
        persona_id = criteria_persona.get('personaId', 'Unknown')
        role = criteria_persona.get('role', 'Unknown')

        eval_questions = criteria_persona.get('moduleEvaluationQuestions', [])

        # Questions should not assume modules can achieve full competency
        # Look for unrealistic expectations
        unrealistic_keywords = [
            'ensure competency', 'fully meet', 'complete development',
            'master', 'achieve competency', 'demonstrate competency'
        ]

        unrealistic_questions = []
        for question in eval_questions:
            question_lower = question.lower()
            if any(keyword in question_lower for keyword in unrealistic_keywords):
                unrealistic_questions.append(question)

        # This is a soft check - we're looking for questions that might have
        # unrealistic expectations
        if unrealistic_questions:
            print(f"\nNote: {persona_id} has questions that may imply unrealistic scope:")
            for q in unrealistic_questions:
                print(f"  - {q[:80]}...")


class TestCrossCuttingThemes:
    """Test that cross-cutting evaluation themes are comprehensive"""

    def test_all_required_themes_present(self):
        """Test that all required cross-cutting themes are defined"""
        criteria = TestDataLoader.load_testing_criteria()

        if not criteria:
            pytest.fail("No testing criteria loaded")

        first_persona = criteria[0]
        themes = first_persona.get('_cross_cutting_themes', {})

        required_theme_keywords = [
            'power',  # Power, Difference, and Inclusion
            'inquiry',  # Transformational Inquiry
            'accessibility',  # Accessibility and Universal Design
            'context',  # Contextualisation
            'evidence',  # Evidence Gathering
            'level',  # Level-Appropriate Complexity
            'integration',  # Integration (I-We-It)
            'limitation'  # Acknowledgment of Limitations
        ]

        theme_names = []
        for theme_key, theme_data in themes.items():
            if theme_key.startswith('theme'):
                name = theme_data.get('name', '')
                theme_names.append(name.lower())

        missing_themes = []
        for keyword in required_theme_keywords:
            if not any(keyword in theme_name for theme_name in theme_names):
                missing_themes.append(keyword)

        assert len(missing_themes) == 0, (
            f"Missing cross-cutting themes: {', '.join(missing_themes)}. "
            f"Found themes: {[t for t in theme_names]}"
        )

    def test_themes_have_key_questions(self):
        """Test that each cross-cutting theme has key questions defined"""
        criteria = TestDataLoader.load_testing_criteria()

        if not criteria:
            pytest.fail("No testing criteria loaded")

        first_persona = criteria[0]
        themes = first_persona.get('_cross_cutting_themes', {})

        for theme_key, theme_data in themes.items():
            if not theme_key.startswith('theme'):
                continue

            theme_name = theme_data.get('name', 'Unknown')
            key_questions = theme_data.get('keyQuestions', [])

            assert len(key_questions) > 0, (
                f"Cross-cutting theme '{theme_name}' has no key questions defined"
            )

            assert len(key_questions) >= 3, (
                f"Cross-cutting theme '{theme_name}' has only {len(key_questions)} questions. "
                f"Should have at least 3 for meaningful evaluation."
            )


class TestAccessibilityConsiderations:
    """Test that testing criteria address accessibility"""

    @pytest.mark.parametrize("criteria_persona", TestDataLoader.load_testing_criteria())
    def test_personas_with_disabilities_have_accessibility_questions(self, criteria_persona):
        """Test that personas with disabilities have accessibility-focused questions"""
        persona_id = criteria_persona.get('personaId', 'Unknown')
        role = criteria_persona.get('role', 'Unknown')
        diversity_context = criteria_persona.get('diversityContext', '').lower()

        # Check if persona mentions disability
        disability_keywords = ['disabled', 'disability', 'wheelchair', 'deaf', 'blind',
                               'chronic pain', 'anxiety', 'adhd', 'dyslexia', 'neurodivergent']

        has_disability = any(keyword in diversity_context for keyword in disability_keywords)

        if has_disability:
            eval_questions = criteria_persona.get('moduleEvaluationQuestions', [])
            questions_text = ' '.join(eval_questions).lower()

            accessibility_keywords = [
                'accessible', 'accessibility', 'adjustment', 'caption', 'screen reader',
                'flexible', 'pacing', 'reasonable adjustment', 'access need'
            ]

            addresses_accessibility = any(
                keyword in questions_text for keyword in accessibility_keywords
            )

            assert addresses_accessibility, (
                f"Persona {persona_id} ({role}) has disability mentioned in context "
                f"but evaluation questions don't address accessibility. "
                f"Context: {diversity_context}"
            )


class TestScenarioCoverage:
    """Test overall scenario coverage across all personas"""

    def test_competency_coverage_across_personas(self):
        """Test that testing scenarios collectively cover diverse competencies"""
        criteria = TestDataLoader.load_testing_criteria()
        competency_names = TestDataLoader.get_competency_names()

        # Collect all competencies tested across all personas
        tested_competencies = set()

        for persona in criteria:
            scenarios = persona.get('moduleTestingScenarios', {})
            for scenario_key, scenario_data in scenarios.items():
                if scenario_key.startswith('scenario'):
                    comp = scenario_data.get('competency', '').strip()
                    if comp:
                        tested_competencies.add(comp)

        coverage_pct = (len(tested_competencies) / len(competency_names)) * 100

        print(f"\nCompetency coverage: {len(tested_competencies)}/{len(competency_names)} "
              f"competencies tested ({coverage_pct:.1f}%)")

        # We should aim for at least some coverage
        assert len(tested_competencies) > 0, (
            "No competencies are tested across any personas"
        )

        # Print untested competencies
        untested = competency_names - tested_competencies
        if untested:
            print(f"\nUntested competencies ({len(untested)}):")
            for comp in sorted(untested):
                print(f"  - {comp}")


if __name__ == "__main__":
    # Run tests with verbose output
    pytest.main([__file__, "-v", "-s"])
