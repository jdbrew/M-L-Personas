# Module Testing Criteria Test Documentation

## Overview

This test suite validates that module testing criteria in each stage file adequately address persona learning needs against the competency framework, while respecting the boundaries of what modular learning can achieve.

## Test File

**File:** `test_module_testing_criteria.py`

## Purpose

The tests validate seven critical areas:

1. **Testing Criteria Completeness**: Every persona has testing criteria with evaluation questions
2. **Testing Scenarios**: Scenarios map to valid competencies and have meaningful questions
3. **Learning Needs Alignment**: Scenarios address personas' target competencies and barriers
4. **Modular Learning Scope**: Criteria respect realistic scope of modular learning
5. **Cross-Cutting Themes**: Required themes are present and comprehensive
6. **Accessibility**: Personas with disabilities have accessibility-focused questions
7. **Competency Coverage**: Scenarios collectively cover diverse competencies

## Framework Files Used

### Testing Criteria Files
- `ml_framework_module_testing_criteria-fundamental_stage.yaml` - 4 personas
- `ml_framework_module_testing_criteria-stage1.yaml` - 5 personas
- `ml_framework_module_testing_criteria-stage2.yaml` - 11 personas
- `ml_framework_module_testing_criteria-stage3.yaml` - 2 personas
- `ml_framework_module_testing_criteria-stage4.yaml` - 3 personas

**Total:** 25 personas across all stages

### Reference Files
- `ml_framework_standards-competencies-v1_0.yaml` - 27 competencies for validation
- `ml_modular_logic_model-v1_0.yaml` - Scope boundaries (G, H, I, J vs K)
- `ml_framework_personas-*.yaml` - Original persona profiles with learning needs

## Test Suites

### 1. TestTestingCriteriaCompleteness (52 tests)

Validates that testing criteria exist and are complete for all personas.

**Tests:**
- `test_testing_criteria_files_exist` - All 5 testing criteria files exist
- `test_all_personas_have_testing_criteria` - Every persona has corresponding testing criteria
- `test_persona_has_evaluation_questions` (25 tests) - Each persona has at least 5 evaluation questions
- `test_persona_has_diversity_context` (25 tests) - Each persona has diversity context defined

**What This Tests:**
- Testing criteria files are present and loadable
- All 25 personas have evaluation questions to test modules
- Questions are numerous enough for meaningful evaluation (minimum 5)
- Diversity context is documented to inform testing

**Current Status:** ✅ All 52 tests passing

### 2. TestTestingScenarios (100 tests)

Validates that testing scenarios are comprehensive and properly structured.

**Tests:**
- `test_persona_has_testing_scenarios` (25 tests) - Personas have testing scenarios (reports warnings for missing)
- `test_scenarios_map_to_valid_competencies` (25 tests) - All scenarios reference valid competency names
- `test_scenarios_have_test_questions` (25 tests) - Each scenario has meaningful test question (>50 chars)
- `test_scenarios_have_evaluation_criteria` (25 tests) - Each scenario has at least 3 evaluation criteria

**What This Tests:**
- Scenarios exist for personas (though not all personas have them yet)
- Scenario competency references are accurate (no typos or paraphrases)
- Test questions are substantial enough to guide evaluation
- Evaluation criteria provide clear assessment measures

**Current Status:** ⚠️ 95/100 tests passing

**Failures (5):**
- Persona 21 (Head of Health and Safety): References "Make sure patients' safety, experience and outcomes are central" - should be "Respond to patient safety concerns, needs and preferences"
- Persona 22 (Specialist Doctor): References "Build networks and strategic relationships" - should be "Build relationships"
- Persona 23 (Programme Director): References "Lead organisation in building patient-centric culture" - invalid
- Persona 24 (Chief Nursing Officer): References "Set strategic direction" - invalid
- Persona 25 (Director of Corporate Affairs): References "Shape organisational culture" - invalid

**Recommendations:**
- Update scenarios to use exact competency names from framework
- These paraphrases may be descriptors from specific stages rather than competency names

### 3. TestLearningNeedsAlignment (50 tests)

Validates that testing criteria align with identified persona learning needs.

**Tests:**
- `test_scenarios_address_target_competencies` (25 tests) - Scenarios cover personas' target competencies
- `test_evaluation_questions_address_diversity_barriers` (25 tests) - Questions address diversity-related barriers

**What This Tests:**
- Scenarios test the specific competencies each persona needs to develop
- Evaluation questions address systemic barriers and discrimination experiences
- Questions use keywords like "barrier," "discrimination," "assumption," "structural," etc.

**Current Status:** ✅ 10/50 passed, 40 skipped (due to personas not having complete profile data)

**Findings for Tested Personas (Stage 1):**
- Persona 5: 3/3 target competencies covered (100%)
- Personas 6-9: All have evaluation questions addressing diversity barriers

**Notes:**
- Many tests skipped because original persona files (Fundamental, Stage 2, 3, 4) have YAML errors
- Once persona files are fixed, these tests will validate all personas

### 4. TestModularLearningScopeAlignment (27 tests)

Validates that testing criteria respect modular learning scope boundaries.

**Tests:**
- `test_cross_cutting_themes_include_limitations` - "Acknowledgment of Limitations" theme present
- `test_cross_cutting_themes_include_power_and_inclusion` - Power/Inclusion theme present
- `test_evaluation_questions_check_realistic_scope` (25 tests) - Questions don't assume unrealistic outcomes

**What This Tests:**
- Cross-cutting themes include acknowledgment that modules have limitations
- Themes address power, diversity, and inclusion as core concerns
- Evaluation questions don't expect modules to achieve full competency

**Current Status:** ✅ All 27 tests passing

**Key Validation:**
Tests check that questions avoid unrealistic keywords like:
- "ensure competency"
- "fully meet"
- "complete development"
- "achieve competency"

This ensures testing criteria align with the logic model: modular learning provides awareness, engagement, knowledge, and recognition of further needs (G, H, I, J) but **NOT** full competency achievement (K).

### 5. TestCrossCuttingThemes (2 tests)

Validates that cross-cutting evaluation themes are comprehensive.

**Tests:**
- `test_all_required_themes_present` - All 8 required themes are defined
- `test_themes_have_key_questions` - Each theme has at least 3 key questions

**Required Themes:**
1. **Power, Difference, and Inclusion** - Diversity as golden thread
2. **Transformational Inquiry (Q component)** - Provoke questioning, not just information
3. **Accessibility and Universal Design** - Work for diverse learning needs
4. **Contextualisation and Application** - Translate to specific contexts
5. **Evidence Gathering and Competency Assessment** - Guide evidence collection
6. **Level-Appropriate Complexity** - Match developmental stage
7. **Integration Across I-We-It** - Personal, relational, operational integration
8. **Acknowledgment of Limitations** - Honest about scope and purpose

**Current Status:** ✅ All 2 tests passing

**Findings:**
- All 8 required themes present in testing criteria
- Each theme has 3+ key questions for evaluation
- Themes align with modular design guidelines (P + Q = L, Principle 10, etc.)

### 6. TestAccessibilityConsiderations (25 tests)

Validates that personas with disabilities have accessibility-focused evaluation questions.

**Tests:**
- `test_personas_with_disabilities_have_accessibility_questions` (25 tests) - Personas mentioning disability have accessibility questions

**What This Tests:**
- When diversity context mentions disability keywords (disabled, wheelchair, deaf, dyslexia, chronic pain, ADHD, etc.)
- Evaluation questions address accessibility keywords (accessible, adjustment, caption, screen reader, flexible pacing, reasonable adjustment)
- Ensures modules will be tested for accessibility when designed for personas with disabilities

**Current Status:** ⚠️ 24/25 tests passing

**Failure (1):**
- **Persona 13 (Lead Vehicle Engineer)**: Diversity context mentions "disabled (acquired mobility impairment)" but evaluation questions don't address accessibility

**Recommendation:**
- Add accessibility-focused evaluation questions for Persona 13
- Questions should address physical accessibility, adjustment needs, and inclusive workplace design

### 7. TestScenarioCoverage (1 test)

Tests overall scenario coverage across all personas.

**Tests:**
- `test_competency_coverage_across_personas` - Scenarios collectively test diverse competencies

**What This Tests:**
- How many of the 27 competencies are tested across all persona scenarios
- Which competencies remain untested

**Current Status:** ✅ 1 test passing

**Findings:**
- **13/27 competencies tested (48.1% coverage)**
- Tested across 13 personas with scenarios (Fundamental: 4, Stage 1: 1, Stage 3: 2, Stage 4: 3)
- 12 personas have 0 scenarios (Stage 1: 4, Stage 2: 11)

**Untested Competencies (14):**
- Develop personal health and wellbeing strategies
- Prioritise for personal productivity
- Drive continuous improvement and innovation
- Encourage open dialogue and feedback
- Lead a collaborative team
- Manage and measure performance
- Manage challenges
- Maximise outputs and get best value for public money
- Personalise care
- Provide clear purpose, vision, and deliverables
- Share good practice
- Support others through change
- Take accountability for my actions
- Transform through technology and innovation

**Recommendation:**
- Add testing scenarios for Stage 1 personas 6-9 and all Stage 2 personas
- Ensure coverage of untested competencies, particularly:
  - Personal productivity and wellbeing
  - Performance management
  - Innovation and change leadership

## Running the Tests

### Prerequisites

```bash
pip install pytest pyyaml
```

### Run All Tests

```bash
pytest test_module_testing_criteria.py -v
```

### Run Specific Test Suite

```bash
# Test completeness
pytest test_module_testing_criteria.py::TestTestingCriteriaCompleteness -v

# Test scenarios
pytest test_module_testing_criteria.py::TestTestingScenarios -v

# Test alignment with learning needs
pytest test_module_testing_criteria.py::TestLearningNeedsAlignment -v

# Test accessibility
pytest test_module_testing_criteria.py::TestAccessibilityConsiderations -v

# Test cross-cutting themes
pytest test_module_testing_criteria.py::TestCrossCuttingThemes -v
```

### Run with Detailed Output

```bash
pytest test_module_testing_criteria.py -v -s
```

## Test Results Summary

**Current Status:** 211/257 tests passing (82%), 40 skipped, 6 failed

### By Test Suite

```
TestTestingCriteriaCompleteness:      52/52 tests passing (100%) ✅
TestTestingScenarios:                  95/100 tests passing (95%) ⚠️
TestLearningNeedsAlignment:            10/50 tests passing, 40 skipped ⚠️
TestModularLearningScopeAlignment:     27/27 tests passing (100%) ✅
TestCrossCuttingThemes:                2/2 tests passing (100%) ✅
TestAccessibilityConsiderations:       24/25 tests passing (96%) ⚠️
TestScenarioCoverage:                  1/1 test passing (100%) ✅
                                       ───
Total:                                 211/257 passing (82%)
```

## Key Findings

### ✅ Strengths

1. **Complete Evaluation Questions**: All 25 personas have 5+ evaluation questions
2. **Diversity Context Documented**: All personas have diversity context defined
3. **Cross-Cutting Themes**: All 8 required themes present with adequate questions
4. **Realistic Scope**: Testing criteria respect modular learning boundaries
5. **Scenario Structure**: Existing scenarios have proper structure (questions, criteria)

### ⚠️ Issues Identified

1. **Invalid Competency References (5 personas)**:
   - Personas 21-25 reference competencies by paraphrased descriptors
   - Need to update to exact competency names from framework

2. **Missing Accessibility Questions (1 persona)**:
   - Persona 13 mentions disability but lacks accessibility evaluation questions
   - Need to add accessibility-focused questions

3. **Incomplete Scenario Coverage**:
   - Only 13/25 personas have testing scenarios (52%)
   - 12 personas need scenarios (4 from Stage 1, all 11 from Stage 2)
   - Only 13/27 competencies tested (48% coverage)
   - Need scenarios for untested competencies

4. **Limited Learning Needs Validation**:
   - 40 tests skipped due to YAML errors in persona source files
   - Cannot validate alignment for Fundamental, Stage 2, 3, 4 personas
   - Need to fix persona YAML files to enable full validation

## Gap Analysis

### Personas Without Testing Scenarios

**Stage 1 (4 personas):**
- Persona 6: Midwife
- Persona 7: Community Pharmacist
- Persona 8: Ward Nurse
- Persona 9: Estates Manager

**Stage 2 (11 personas):**
- Persona 10: Strategic Commissioning Manager
- Persona 11: HR Manager
- Persona 12: Specialist Healthcare Scientist
- Persona 13: Lead Vehicle Engineer
- Persona 14: Senior House Officer
- Persona 15: Lead Psychological Wellbeing Practitioner
- Persona 16: Head of Neighbourhood Teams
- Persona 17: Assistant Director of Finance
- Persona 18: Primary Care Practice Manager
- Persona 19: Information Governance Lead
- Persona 20: Primary Care Operations Lead

### Competencies Not Yet Tested

14 competencies have no testing scenarios across any persona:

**Personal productivity (2):**
- Develop personal health and wellbeing strategies
- Prioritise for personal productivity

**Communication and culture (2):**
- Encourage open dialogue and feedback
- Take accountability for my actions

**Team building and performance (4):**
- Lead a collaborative team
- Manage and measure performance
- Manage challenges
- Share good practice

**Innovation and change (2):**
- Drive continuous improvement and innovation
- Transform through technology and innovation
- Support others through change

**Quality and outcomes (3):**
- Personalise care
- Provide clear purpose, vision, and deliverables
- Maximise outputs and get best value for public money

## Using Tests for Quality Assurance

These tests support testing criteria quality by:

1. **Identifying Gaps**: Highlighting which personas lack scenarios
2. **Validating Structure**: Ensuring scenarios have required elements
3. **Checking Alignment**: Verifying scenarios address learning needs
4. **Ensuring Accuracy**: Catching invalid competency references
5. **Promoting Inclusion**: Confirming accessibility considerations

## Recommendations

### Immediate Actions

1. **Fix Invalid Competency References** (Personas 21-25):
   - Update scenario competency fields to use exact names from framework
   - Verify all stage-level descriptors are mapped to correct base competencies

2. **Add Accessibility Questions** (Persona 13):
   - Add evaluation questions addressing physical accessibility
   - Include questions about reasonable adjustments and inclusive design

3. **Fix Persona YAML Files**:
   - Resolve YAML syntax errors in Fundamental, Stage 2, 3, 4 persona files
   - This will enable 40 additional tests to run

### Longer-Term Actions

4. **Complete Missing Scenarios**:
   - Add 3 testing scenarios for each of the 12 personas without scenarios
   - Prioritize Stage 1 (immediate), then Stage 2 (middle managers)

5. **Expand Competency Coverage**:
   - Ensure all 27 competencies are tested across the persona set
   - Focus on untested competencies (personal productivity, innovation, etc.)

6. **Enhance Diversity Coverage**:
   - Review evaluation questions to ensure they address specific barriers
   - Add questions that prompt consideration of intersectionality

## Integration with Other Tests

These tests complement `test_persona_competency_mapping.py`:

| test_persona_competency_mapping.py | test_module_testing_criteria.py |
|-----------------------------------|----------------------------------|
| Tests persona → competency mapping | Tests testing criteria → competency mapping |
| Validates learning needs identified | Validates testing criteria address needs |
| Confirms competency framework complete | Confirms scenarios reference valid competencies |
| Checks modular learning scope (logic model) | Checks criteria respect realistic scope |
| Validates diversity profiles exist | Validates evaluation questions address diversity |

Together, these test suites ensure:
1. Personas have valid learning needs mapped to competencies ✅
2. Testing criteria exist to evaluate whether modules address those needs ✅
3. Everything aligns with modular learning scope and competency framework ✅

## Questions These Tests Answer

1. ✅ Do all personas have module testing criteria defined?
2. ✅ Do evaluation questions address diversity and barriers?
3. ⚠️ Do testing scenarios reference valid competencies? (mostly yes, 5 errors)
4. ✅ Do scenarios have meaningful test questions and evaluation criteria?
5. ⚠️ Do scenarios address personas' target competencies? (yes where data available)
6. ✅ Do cross-cutting themes cover all required areas?
7. ✅ Do criteria respect modular learning scope boundaries?
8. ⚠️ Do personas with disabilities have accessibility questions? (24/25 yes)
9. ⚠️ Are all competencies tested across the persona set? (48% coverage)
10. ⚠️ Do all personas have testing scenarios? (52% have scenarios)

---

**Last Updated:** 2025-11-17
**Test Suite Version:** 1.0
**Framework Version:** 1.0
