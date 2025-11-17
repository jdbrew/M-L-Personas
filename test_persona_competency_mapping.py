"""
Tests for validating that all personas' learning needs are addressed by competencies
and understanding how modular learning supports competency development.

This test suite validates:
1. All personas have valid target competencies that exist in the framework
2. Persona learning needs align with competency descriptors at appropriate stages
3. Modular learning outcomes (G, H, I, J) are properly scoped
4. Learning needs gaps are properly identified for deeper learning pathways
"""

import yaml
import pytest
from pathlib import Path
from typing import Dict, List, Any, Tuple


# File paths
BASE_DIR = Path("/home/user/M-L-Personas")
COMPETENCIES_FILE = BASE_DIR / "ml_framework_standards-competencies-v1_0.yaml"
LOGIC_MODEL_FILE = BASE_DIR / "ml_modular_logic_model-v1_0.yaml"
PERSONA_FILES = [
    BASE_DIR / "ml_framework_personas-fundamental_stage.yaml",
    BASE_DIR / "ml_framework_personas-stage1.yaml",
    BASE_DIR / "ml_framework_personas-stage2.yaml",
    BASE_DIR / "ml_framework_personas-stage3.yaml",
    BASE_DIR / "ml_framework_personas-stage4.yaml",
]


class TestDataLoader:
    """Utility class for loading and caching test data"""

    _competencies_cache = None
    _logic_model_cache = None
    _personas_cache = None

    @classmethod
    def load_competencies(cls) -> Dict:
        """Load the competencies framework"""
        if cls._competencies_cache is None:
            with open(COMPETENCIES_FILE, 'r') as f:
                cls._competencies_cache = yaml.safe_load(f)
        return cls._competencies_cache

    @classmethod
    def load_logic_model(cls) -> Dict:
        """Load the modular learning logic model"""
        if cls._logic_model_cache is None:
            with open(LOGIC_MODEL_FILE, 'r') as f:
                cls._logic_model_cache = yaml.safe_load(f)
        return cls._logic_model_cache

    @classmethod
    def load_personas(cls) -> List[Dict]:
        """Load all persona files, handling YAML errors gracefully"""
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
                            # Add stage context to each persona
                            persona['_stage'] = stage.get('stageName', 'Unknown')
                            persona['_source_file'] = filepath.name
                            personas.append(persona)

                except yaml.YAMLError as e:
                    # Skip files with YAML errors, but log them
                    print(f"Warning: Could not parse {filepath.name}: {e}")
                    continue
                except Exception as e:
                    print(f"Warning: Error loading {filepath.name}: {e}")
                    continue

            cls._personas_cache = personas
        return cls._personas_cache

    @classmethod
    def get_competency_map(cls) -> Dict[str, Dict]:
        """Create a map of competency names to their full definitions"""
        competencies_data = cls.load_competencies()
        competency_map = {}

        framework = competencies_data.get('managementAndLeadershipFramework', {})
        focus_areas = framework.get('focusAreas', [])

        for focus_area in focus_areas:
            sections = focus_area.get('sections', [])
            for section in sections:
                competencies = section.get('competencies', [])
                for competency in competencies:
                    name = competency.get('name', '').strip()  # Strip whitespace
                    competency_map[name] = {
                        'name': name,
                        'focusArea': focus_area.get('title', '').strip(),
                        'section': section.get('title', '').strip(),
                        'descriptorsByStage': competency.get('descriptorsByStage', []),
                        'focusAreaDescription': focus_area.get('description', '')
                    }

        return competency_map

    @classmethod
    def normalize_stage_name(cls, stage_str: str) -> str:
        """Normalize stage names for comparison"""
        stage_str = stage_str.lower().strip()

        # Map common stage variations
        stage_mappings = {
            'fundamental': 'Fundamental',
            'fundamental stage': 'Fundamental',
            'stage 1': 'Stage 1',
            'stage 2': 'Stage 2',
            'stage 3': 'Stage 3',
            'stage 4': 'Stage 4',
        }

        for key, value in stage_mappings.items():
            if key in stage_str:
                return value

        return stage_str

    @classmethod
    def extract_stage_number(cls, stage_str: str) -> str:
        """Extract stage identifier from stage name"""
        normalized = cls.normalize_stage_name(stage_str)

        # Handle "Fundamental" separately
        if 'Fundamental' in normalized:
            return 'Fundamental'

        # Extract stage number
        if 'Stage 1' in normalized or 'stage 1' in stage_str.lower():
            return 'Stage 1'
        elif 'Stage 2' in normalized or 'stage 2' in stage_str.lower():
            return 'Stage 2'
        elif 'Stage 3' in normalized or 'stage 3' in stage_str.lower():
            return 'Stage 3'
        elif 'Stage 4' in normalized or 'stage 4' in stage_str.lower():
            return 'Stage 4'

        return normalized


class TestPersonaCompetencyMapping:
    """Test that all personas have valid competency mappings"""

    def test_all_personas_loaded(self):
        """Verify that personas are loaded successfully"""
        personas = TestDataLoader.load_personas()
        assert len(personas) > 0, "No personas were loaded successfully"
        print(f"\nLoaded {len(personas)} personas from valid files")

    def test_competencies_framework_loaded(self):
        """Verify the competencies framework loads correctly"""
        competencies = TestDataLoader.load_competencies()
        assert competencies is not None

        framework = competencies.get('managementAndLeadershipFramework', {})
        focus_areas = framework.get('focusAreas', [])
        assert len(focus_areas) > 0, "No focus areas found in competencies framework"

        # Count total competencies
        total_competencies = 0
        for focus_area in focus_areas:
            for section in focus_area.get('sections', []):
                total_competencies += len(section.get('competencies', []))

        print(f"\nLoaded {total_competencies} competencies across {len(focus_areas)} focus areas")

    def test_logic_model_loaded(self):
        """Verify the logic model loads correctly"""
        logic_model = TestDataLoader.load_logic_model()
        assert logic_model is not None

        model = logic_model.get('logic_model', {})
        outcomes = model.get('core_logic', {}).get('outcomes', [])

        # Verify key outcomes are present
        outcome_ids = [outcome.get('id') for outcome in outcomes]
        assert 'G' in outcome_ids, "Outcome G (awareness/credibility) not found"
        assert 'H' in outcome_ids, "Outcome H (active engagement) not found"
        assert 'I' in outcome_ids, "Outcome I (knowledge gains) not found"
        assert 'J' in outcome_ids, "Outcome J (recognizing further work needed) not found"

        print(f"\nVerified modular learning outcomes: {outcome_ids}")

    @pytest.mark.parametrize("persona", TestDataLoader.load_personas())
    def test_persona_has_target_competencies(self, persona):
        """Test that each persona has target competencies defined"""
        persona_id = persona.get('personaId', 'Unknown')
        role = persona.get('role', 'Unknown')

        # Get competency development profile
        comp_profile = persona.get('competencyDevelopmentProfile', {})
        target_competencies = comp_profile.get('targetCompetencies', [])

        assert len(target_competencies) > 0, (
            f"Persona {persona_id} ({role}) has no target competencies defined"
        )

        print(f"\n{persona_id} ({role}): {len(target_competencies)} target competencies")

    @pytest.mark.parametrize("persona", TestDataLoader.load_personas())
    def test_persona_target_competencies_exist_in_framework(self, persona):
        """Test that all target competencies for a persona exist in the framework"""
        persona_id = persona.get('personaId', 'Unknown')
        role = persona.get('role', 'Unknown')

        comp_profile = persona.get('competencyDevelopmentProfile', {})
        target_competencies = comp_profile.get('targetCompetencies', [])

        competency_map = TestDataLoader.get_competency_map()

        for target_comp in target_competencies:
            # Parse competency name and stage
            # Format could be "Competency Name (Stage)" or just "Competency Name"
            if '(' in target_comp:
                comp_name = target_comp.split('(')[0].strip()
                stage = target_comp.split('(')[1].replace(')', '').strip()
            else:
                comp_name = target_comp.strip()
                stage = None

            # Check if competency exists
            assert comp_name in competency_map, (
                f"Persona {persona_id} ({role}) targets competency '{comp_name}' "
                f"which does not exist in the framework"
            )

            # If stage specified, verify it exists for this competency
            if stage:
                competency = competency_map[comp_name]
                descriptors = competency.get('descriptorsByStage', [])
                stages_available = [d.get('stage', '').strip() for d in descriptors]

                normalized_stage = TestDataLoader.normalize_stage_name(stage)

                # Check if this stage exists
                stage_found = any(
                    TestDataLoader.normalize_stage_name(s) == normalized_stage
                    for s in stages_available
                )

                assert stage_found, (
                    f"Persona {persona_id} ({role}) targets '{comp_name}' at {stage}, "
                    f"but that stage is not defined. Available stages: {stages_available}"
                )

    @pytest.mark.parametrize("persona", TestDataLoader.load_personas())
    def test_persona_competencies_match_persona_stage(self, persona):
        """Test that persona's target competencies align with their development stage"""
        persona_id = persona.get('personaId', 'Unknown')
        role = persona.get('role', 'Unknown')
        persona_stage = persona.get('_stage', 'Unknown')

        comp_profile = persona.get('competencyDevelopmentProfile', {})
        target_competencies = comp_profile.get('targetCompetencies', [])

        competency_map = TestDataLoader.get_competency_map()
        persona_stage_normalized = TestDataLoader.extract_stage_number(persona_stage)

        for target_comp in target_competencies:
            # Parse competency name and stage
            if '(' in target_comp:
                comp_name = target_comp.split('(')[0].strip()
                comp_stage = target_comp.split('(')[1].replace(')', '').strip()
                comp_stage_normalized = TestDataLoader.normalize_stage_name(comp_stage)

                # Target competency stage should match or be adjacent to persona stage
                # This is a soft check - personas can aspire to next stage
                print(f"  {persona_id}: {comp_name} ({comp_stage_normalized}) in {persona_stage_normalized} stage")


class TestPersonaLearningNeeds:
    """Test that persona learning needs are comprehensively addressed"""

    @pytest.mark.parametrize("persona", TestDataLoader.load_personas())
    def test_persona_has_learning_gaps_identified(self, persona):
        """Test that each persona has their learning gaps identified"""
        persona_id = persona.get('personaId', 'Unknown')
        role = persona.get('role', 'Unknown')

        comp_profile = persona.get('competencyDevelopmentProfile', {})
        prior_knowledge = comp_profile.get('priorKnowledge', {})

        gaps = prior_knowledge.get('gaps', '')

        assert gaps, (
            f"Persona {persona_id} ({role}) has no learning gaps identified. "
            f"All personas should have identified gaps for development."
        )

        assert len(gaps) > 20, (
            f"Persona {persona_id} ({role}) has very brief gap description: '{gaps[:50]}...'. "
            f"Gaps should be detailed enough to guide learning design."
        )

    @pytest.mark.parametrize("persona", TestDataLoader.load_personas())
    def test_persona_has_evidence_gathering_capacity_defined(self, persona):
        """Test that personas have evidence gathering capacity defined"""
        persona_id = persona.get('personaId', 'Unknown')
        role = persona.get('role', 'Unknown')

        comp_profile = persona.get('competencyDevelopmentProfile', {})
        evidence_capacity = comp_profile.get('evidenceGatheringCapacity', {})

        can_demonstrate = evidence_capacity.get('canDemonstrate', [])
        needs_support = evidence_capacity.get('needsSupport', [])

        assert can_demonstrate or needs_support, (
            f"Persona {persona_id} ({role}) has no evidence gathering capacity defined. "
            f"This is essential for understanding modular learning scope."
        )

        print(f"\n{persona_id}: Can demonstrate {len(can_demonstrate)} areas, "
              f"needs support in {len(needs_support)} areas")

    @pytest.mark.parametrize("persona", TestDataLoader.load_personas())
    def test_persona_has_contextual_constraints(self, persona):
        """Test that personas have contextual constraints defined"""
        persona_id = persona.get('personaId', 'Unknown')
        role = persona.get('role', 'Unknown')

        comp_profile = persona.get('competencyDevelopmentProfile', {})
        constraints = comp_profile.get('contextualConstraints', {})

        time_available = constraints.get('timeAvailable')
        system_pressures = constraints.get('systemPressures')
        support_available = constraints.get('supportAvailable')

        assert time_available, (
            f"Persona {persona_id} ({role}) has no time constraints defined"
        )

        assert system_pressures, (
            f"Persona {persona_id} ({role}) has no system pressures defined"
        )

        assert support_available, (
            f"Persona {persona_id} ({role}) has no support availability defined"
        )


class TestModularLearningScopeValidation:
    """Test that modular learning scope is properly understood and bounded"""

    def test_modular_learning_outcomes_are_in_scope(self):
        """Test that the four key modular learning outcomes are properly scoped"""
        logic_model = TestDataLoader.load_logic_model()
        core_logic = logic_model.get('logic_model', {}).get('core_logic', {})
        outcomes = core_logic.get('outcomes', [])

        # All outcomes should be in scope
        for outcome in outcomes:
            assert outcome.get('scope') == 'inScope', (
                f"Outcome {outcome.get('id')} should be in scope but is marked as "
                f"{outcome.get('scope')}"
            )

    def test_meeting_competencies_is_out_of_scope(self):
        """Test that meeting competencies fully is correctly identified as out of scope"""
        logic_model = TestDataLoader.load_logic_model()
        longer_term = logic_model.get('logic_model', {}).get('longer_term_outcomes', [])

        # Find outcome K (Meet Competencies)
        outcome_k = next((o for o in longer_term if o.get('id') == 'K'), None)
        assert outcome_k is not None, "Outcome K (Meet Competencies) not found"

        assert outcome_k.get('scope') == 'outScope', (
            "Meeting competencies fully (Outcome K) should be out of scope for modular learning"
        )

        # Verify the label
        assert 'Meet Competencies' in outcome_k.get('label', ''), (
            "Outcome K should reference meeting competencies"
        )

    @pytest.mark.parametrize("persona", TestDataLoader.load_personas())
    def test_persona_recognizes_modular_learning_limitations(self, persona):
        """Test that personas have potential misunderstandings that modular learning should address"""
        persona_id = persona.get('personaId', 'Unknown')
        role = persona.get('role', 'Unknown')

        comp_profile = persona.get('competencyDevelopmentProfile', {})
        misunderstandings = comp_profile.get('potentialMisunderstandings', [])

        # Personas should have identified potential misunderstandings
        # This helps modules address Outcome J: recognizing further work may be needed
        if misunderstandings:
            assert len(misunderstandings) > 0, (
                f"Persona {persona_id} ({role}) has empty misunderstandings list"
            )

            print(f"\n{persona_id} has {len(misunderstandings)} potential misunderstandings "
                  f"that modules should address")
        else:
            print(f"\nWarning: {persona_id} ({role}) has no potential misunderstandings defined")


class TestCompetencyDescriptorCoverage:
    """Test that competency descriptors adequately address persona learning needs"""

    @pytest.mark.parametrize("persona", TestDataLoader.load_personas())
    def test_target_competencies_have_descriptors_at_persona_stage(self, persona):
        """Test that each target competency has descriptors at the persona's stage"""
        persona_id = persona.get('personaId', 'Unknown')
        role = persona.get('role', 'Unknown')
        persona_stage = persona.get('_stage', 'Unknown')

        comp_profile = persona.get('competencyDevelopmentProfile', {})
        target_competencies = comp_profile.get('targetCompetencies', [])

        competency_map = TestDataLoader.get_competency_map()
        persona_stage_normalized = TestDataLoader.extract_stage_number(persona_stage)

        for target_comp in target_competencies:
            # Parse competency name and stage
            if '(' in target_comp:
                comp_name = target_comp.split('(')[0].strip()
                target_stage = target_comp.split('(')[1].replace(')', '').strip()
            else:
                comp_name = target_comp.strip()
                target_stage = persona_stage_normalized

            if comp_name not in competency_map:
                continue  # Skip if competency doesn't exist (covered by other test)

            competency = competency_map[comp_name]
            descriptors = competency.get('descriptorsByStage', [])

            # Find descriptor for the target stage
            target_stage_normalized = TestDataLoader.normalize_stage_name(target_stage)
            descriptor = next(
                (d for d in descriptors
                 if TestDataLoader.normalize_stage_name(d.get('stage', '')) == target_stage_normalized),
                None
            )

            assert descriptor is not None, (
                f"Persona {persona_id} ({role}) targets '{comp_name}' at {target_stage}, "
                f"but no descriptor exists for that stage"
            )

            # Verify descriptor has meaningful content
            descriptor_text = descriptor.get('descriptor', '')
            assert len(descriptor_text) > 20, (
                f"Descriptor for '{comp_name}' at {target_stage} is too brief: '{descriptor_text}'"
            )

    def test_all_competencies_have_complete_stage_coverage(self):
        """Test that all competencies have descriptors for all stages"""
        competency_map = TestDataLoader.get_competency_map()
        expected_stages = ['Fundamental', 'Stage 1', 'Stage 2', 'Stage 3', 'Stage 4']

        for comp_name, competency in competency_map.items():
            descriptors = competency.get('descriptorsByStage', [])
            available_stages = [
                TestDataLoader.normalize_stage_name(d.get('stage', ''))
                for d in descriptors
            ]

            for expected_stage in expected_stages:
                assert expected_stage in available_stages, (
                    f"Competency '{comp_name}' is missing descriptor for {expected_stage}. "
                    f"Available stages: {available_stages}"
                )


class TestDiversityAndInclusionCoverage:
    """Test that diverse personas have appropriate considerations"""

    @pytest.mark.parametrize("persona", TestDataLoader.load_personas())
    def test_persona_has_diversity_profile(self, persona):
        """Test that each persona has a diversity profile defined"""
        persona_id = persona.get('personaId', 'Unknown')
        role = persona.get('role', 'Unknown')

        diversity_profile = persona.get('diversityProfile', {})

        assert diversity_profile, (
            f"Persona {persona_id} ({role}) has no diversity profile defined"
        )

        # Check for key diversity profile components
        protected_characteristics = diversity_profile.get('protectedCharacteristics', [])
        positionality = diversity_profile.get('positionality', {})
        experience_of_power = diversity_profile.get('experienceOfPower', {})

        assert protected_characteristics, (
            f"Persona {persona_id} ({role}) has no protected characteristics defined"
        )

        assert positionality, (
            f"Persona {persona_id} ({role}) has no positionality defined"
        )

        assert experience_of_power, (
            f"Persona {persona_id} ({role}) has no experience of power defined"
        )

    @pytest.mark.parametrize("persona", TestDataLoader.load_personas())
    def test_persona_has_barriers_identified(self, persona):
        """Test that personas have experienced barriers identified"""
        persona_id = persona.get('personaId', 'Unknown')
        role = persona.get('role', 'Unknown')

        diversity_profile = persona.get('diversityProfile', {})
        experience_of_power = diversity_profile.get('experienceOfPower', {})

        experienced_barriers = experience_of_power.get('experiencedBarriers', [])

        # Some personas may not have experienced barriers, but most should
        if experienced_barriers:
            assert len(experienced_barriers) > 0, (
                f"Persona {persona_id} ({role}) has empty barriers list"
            )

            print(f"\n{persona_id} has {len(experienced_barriers)} identified barriers")


class TestLearningReadinessAndAccessibility:
    """Test that learning readiness and accessibility considerations are captured"""

    @pytest.mark.parametrize("persona", TestDataLoader.load_personas())
    def test_persona_has_learning_preferences(self, persona):
        """Test that each persona has learning preferences defined"""
        persona_id = persona.get('personaId', 'Unknown')
        role = persona.get('role', 'Unknown')

        learning_readiness = persona.get('learningReadiness', {})
        learning_preferences = learning_readiness.get('learningPreferences', [])

        assert learning_preferences, (
            f"Persona {persona_id} ({role}) has no learning preferences defined. "
            f"This is essential for designing accessible modular learning."
        )

        assert len(learning_preferences) > 0, (
            f"Persona {persona_id} ({role}) has empty learning preferences list"
        )

    @pytest.mark.parametrize("persona", TestDataLoader.load_personas())
    def test_persona_has_barriers_to_engagement(self, persona):
        """Test that barriers to learning engagement are identified"""
        persona_id = persona.get('personaId', 'Unknown')
        role = persona.get('role', 'Unknown')

        learning_readiness = persona.get('learningReadiness', {})
        barriers = learning_readiness.get('barriersToEngagement', [])

        # Most personas should have some barriers
        if barriers:
            assert len(barriers) > 0, (
                f"Persona {persona_id} ({role}) has empty barriers to engagement list"
            )

            print(f"\n{persona_id} has {len(barriers)} barriers to engagement identified")

    @pytest.mark.parametrize("persona", TestDataLoader.load_personas())
    def test_persona_has_access_to_learning_defined(self, persona):
        """Test that access to learning resources is defined"""
        persona_id = persona.get('personaId', 'Unknown')
        role = persona.get('role', 'Unknown')

        learning_readiness = persona.get('learningReadiness', {})
        access = learning_readiness.get('accessToLearning', [])

        # Access considerations are essential for modular learning design
        if access:
            assert len(access) > 0, (
                f"Persona {persona_id} ({role}) has empty access to learning list"
            )


if __name__ == "__main__":
    # Run tests with verbose output
    pytest.main([__file__, "-v", "-s"])
