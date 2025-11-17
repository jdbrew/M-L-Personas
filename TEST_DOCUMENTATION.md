# Persona-Competency Testing Documentation

## Overview

This test suite validates that all personas' identified learning needs are addressed by the Management and Leadership Framework competencies, and ensures proper understanding of how modular learning supports (and is bounded in) competency development.

## Test File

**File:** `test_persona_competency_mapping.py`

## Purpose

The tests validate three critical relationships:

1. **Persona → Competency Mapping**: Every persona's target competencies exist in the framework and are properly specified
2. **Learning Needs → Competency Descriptors**: Learning gaps and needs align with competency descriptors at appropriate stages
3. **Modular Learning Scope**: The logic model correctly defines what modular learning can achieve (Outcomes G, H, I, J) versus what requires deeper learning (Outcome K - fully meeting competencies)

## Framework Files Used

### Core Framework Files
- `ml_framework_standards-competencies-v1_0.yaml` - The competencies framework with 27 competencies across 3 focus areas
- `ml_modular_logic_model-v1_0.yaml` - Logic model defining modular learning scope and outcomes
- `ml_framework_personas-fundamental_stage.yaml` - Fundamental stage personas
- `ml_framework_personas-stage1.yaml` - Stage 1 personas
- `ml_framework_personas-stage2.yaml` - Stage 2 personas
- `ml_framework_personas-stage3.yaml` - Stage 3 personas
- `ml_framework_personas-stage4.yaml` - Stage 4 personas

### Competency Framework Structure

The framework contains **27 competencies** organized across **3 focus areas**:

1. **Developing self** (9 competencies)
   - Personal productivity and wellbeing (3)
   - Communicating well (3)
   - Responsibility and integrity (3)

2. **Managing people and resources** (9 competencies)
   - Building teams (3)
   - Performance and delivery (3)
   - Efficiency and effectiveness (3)

3. **Delivering across health and care** (9 competencies)
   - Improving quality (3)
   - Innovation and improvement (3)
   - Working collaboratively (3)

Each competency has descriptors for all 5 stages: Fundamental, Stage 1, Stage 2, Stage 3, and Stage 4.

### Modular Learning Logic Model

The logic model defines what modular learning **can** and **cannot** achieve:

**In Scope** (Outcomes that modular learning supports):
- **Outcome G**: Managers and leaders are **aware** of modular resources and recognize them as credible introductory support
- **Outcome H**: Managers and leaders **engage actively** with modules, experience stimulating inquiry, and value their contribution
- **Outcome I**: Managers and leaders **gain knowledge** (assessed at end of module)
- **Outcome J**: Managers and leaders **recognize further work may be needed** to meet the competency

**Out of Scope** (Requires deeper learning pathways):
- **Outcome K**: Managers and leaders fully **meet competencies**
- **Outcome L**: Intended outcomes of framework are fully realized

This distinction is **critical** - modular learning is designed as an **introduction** that builds awareness, engagement, and foundational knowledge, while recognizing that meeting competencies fully requires additional work including:
- Assessment against competencies (Input B - out of scope)
- Learner actions like journaling, reflection, discussion (Element C - out of scope)
- Signposting to deeper learning (Element D - out of scope)

## Test Suites

### 1. TestPersonaCompetencyMapping (18 tests)

Validates that personas are properly mapped to competencies.

**Tests:**
- `test_all_personas_loaded` - Verifies personas load successfully from YAML files
- `test_competencies_framework_loaded` - Verifies competencies framework loads with all 27 competencies
- `test_logic_model_loaded` - Verifies logic model loads with outcomes G, H, I, J
- `test_persona_has_target_competencies` (5 tests) - Each persona has target competencies defined
- `test_persona_target_competencies_exist_in_framework` (5 tests) - All target competencies exist in framework
- `test_persona_competencies_match_persona_stage` (5 tests) - Target competencies align with persona's developmental stage

**What This Tests:**
- Personas are well-formed and loadable
- All personas identify specific competencies they need to develop
- These competencies actually exist in the framework (no orphaned references)
- The competencies targeted are appropriate for the persona's stage

### 2. TestPersonaLearningNeeds (15 tests)

Validates that persona learning needs are comprehensively identified.

**Tests:**
- `test_persona_has_learning_gaps_identified` (5 tests) - Each persona has detailed learning gaps
- `test_persona_has_evidence_gathering_capacity_defined` (5 tests) - Evidence gathering needs are defined
- `test_persona_has_contextual_constraints` (5 tests) - Time, system pressures, and support constraints are specified

**What This Tests:**
- Personas have clearly articulated learning needs and gaps
- We understand what evidence personas can already demonstrate vs. what they need support with
- Real-world constraints (time, pressure, support) are acknowledged
- These elements help define what modular learning needs to address

### 3. TestModularLearningScopeValidation (7 tests)

Validates that modular learning scope is properly understood and bounded.

**Tests:**
- `test_modular_learning_outcomes_are_in_scope` - Outcomes G, H, I, J are correctly marked as in scope
- `test_meeting_competencies_is_out_of_scope` - Outcome K (meeting competencies) is correctly out of scope
- `test_persona_recognizes_modular_learning_limitations` (5 tests) - Personas have potential misunderstandings identified

**What This Tests:**
- The logic model correctly bounds what modular learning can achieve
- We acknowledge that **modular learning alone does not result in meeting competencies**
- Modular learning provides awareness, engagement, knowledge, and recognition of further needs
- Potential misunderstandings are identified so modules can address them (supporting Outcome J)

**Critical Insight:**
This test suite ensures we maintain realistic expectations. Modular learning is:
- ✅ An introduction and credible starting point
- ✅ A way to gain foundational knowledge
- ✅ A prompt to recognize further development needs
- ❌ NOT sufficient alone to meet competencies
- ❌ NOT a replacement for deeper learning, assessment, and workplace application

### 4. TestCompetencyDescriptorCoverage (6 tests)

Validates that competency descriptors adequately address persona needs.

**Tests:**
- `test_target_competencies_have_descriptors_at_persona_stage` (5 tests) - Each target competency has meaningful descriptors at the persona's stage
- `test_all_competencies_have_complete_stage_coverage` - All 27 competencies have descriptors for all 5 stages

**What This Tests:**
- The framework provides specific guidance for each competency at each stage
- Personas' target stages have corresponding descriptors (not missing stages)
- Descriptors are substantial enough to guide learning design
- Complete coverage ensures no gaps in the framework

### 5. TestDiversityAndInclusionCoverage (10 tests)

Validates that diverse personas have appropriate diversity considerations captured.

**Tests:**
- `test_persona_has_diversity_profile` (5 tests) - Each persona has protected characteristics, positionality, and power experiences defined
- `test_persona_has_barriers_identified` (5 tests) - Experienced barriers to development are identified

**What This Tests:**
- Personas reflect diverse backgrounds (aligning with WRES/WDES workforce data)
- Power, privilege, and marginalization are considered
- Barriers to learning and development are acknowledged
- Modular learning must address these diversity considerations (Design Principle 10)

**Critical for:**
- Ensuring modules address difference, diversity, inclusion, and power as a "golden thread"
- Testing whether modules make assumptions about learners' backgrounds
- Validating that examples and scenarios are inclusive

### 6. TestLearningReadinessAndAccessibility (15 tests)

Validates that learning readiness and accessibility considerations are captured.

**Tests:**
- `test_persona_has_learning_preferences` (5 tests) - Learning preferences are defined
- `test_persona_has_barriers_to_engagement` (5 tests) - Barriers to engagement are identified
- `test_persona_has_access_to_learning_defined` (5 tests) - Access to learning resources is specified

**What This Tests:**
- Diverse learning preferences are acknowledged (practical vs. theoretical, visual vs. text, etc.)
- Barriers like time, technology access, literacy, neurodivergence are identified
- Module design can respond to varied access needs (mobile-friendly, works on limited bandwidth, etc.)

**Critical for:**
- Designing accessible modules that work for diverse learners
- Understanding realistic engagement constraints
- Ensuring modules don't assume privileged access to time, technology, or educational background

## Running the Tests

### Prerequisites

```bash
pip install pytest pyyaml
```

### Run All Tests

```bash
pytest test_persona_competency_mapping.py -v
```

### Run Specific Test Suite

```bash
# Run only persona-competency mapping tests
pytest test_persona_competency_mapping.py::TestPersonaCompetencyMapping -v

# Run only modular learning scope validation tests
pytest test_persona_competency_mapping.py::TestModularLearningScopeValidation -v

# Run only diversity and inclusion tests
pytest test_persona_competency_mapping.py::TestDiversityAndInclusionCoverage -v
```

### Run with Detailed Output

```bash
pytest test_persona_competency_mapping.py -v -s
```

The `-s` flag shows print statements, which provide additional context about personas, competencies, and gaps.

## Test Results Summary

**Current Status:** ✅ All 71 tests passing

```
TestPersonaCompetencyMapping:          18 tests (3 framework + 15 persona-specific)
TestPersonaLearningNeeds:              15 tests (5 personas × 3 need categories)
TestModularLearningScopeValidation:     7 tests (2 scope + 5 persona limitations)
TestCompetencyDescriptorCoverage:       6 tests (5 personas + 1 framework)
TestDiversityAndInclusionCoverage:     10 tests (5 personas × 2 categories)
TestLearningReadinessAndAccessibility: 15 tests (5 personas × 3 categories)
                                       ──
Total:                                 71 tests
```

## Key Findings

### ✅ Validated

1. **Complete Competency Coverage**: All 27 competencies have descriptors for all 5 stages
2. **Persona-Competency Alignment**: All 5 loaded personas have valid target competencies that exist in the framework
3. **Learning Needs Documented**: All personas have:
   - Identified learning gaps
   - Evidence gathering capacity defined
   - Contextual constraints specified
   - Learning preferences and barriers documented
4. **Modular Learning Properly Scoped**: Logic model correctly identifies:
   - What modular learning CAN achieve (G, H, I, J)
   - What it CANNOT achieve alone (K, L)
5. **Diversity Considerations**: All personas have:
   - Diversity profiles with protected characteristics
   - Positionality and power dynamics documented
   - Experienced barriers identified

### ⚠️ Limitations

1. **YAML Parsing Errors**: Some persona files (fundamental, stage 2, 3, 4) have YAML syntax errors and couldn't be fully loaded
   - Only Stage 1 personas (5 personas) are currently being tested
   - Need to fix YAML syntax in other stage files to test all personas

2. **Test Coverage**: Tests currently validate structure and existence but could be extended to:
   - Analyze semantic alignment between gaps and competency descriptors
   - Validate that module testing criteria adequately cover all personas
   - Cross-reference barriers with accessibility requirements

## Interpreting Test Results

### What Passing Tests Mean

When all tests pass, it means:

1. **Structural Integrity**: Personas and frameworks are well-formed and complete
2. **Referential Integrity**: No broken references between personas and competencies
3. **Scope Clarity**: Modular learning boundaries are clearly defined
4. **Inclusive Design**: Diversity and accessibility considerations are documented

### What Failing Tests Indicate

If tests fail, investigate:

1. **Missing Competencies**: A persona references a competency that doesn't exist → Need to either add the competency or fix the persona reference
2. **Missing Stages**: A competency lacks descriptors for a stage → Need to add stage-specific descriptors
3. **Incomplete Persona Profiles**: A persona is missing critical elements → Need to complete the persona definition
4. **Scope Errors**: Outcomes are incorrectly marked as in/out of scope → Need to review logic model

## Using Tests for Module Design

These tests support module design by:

1. **Identifying Target Audiences**: Understand which personas need which competencies
2. **Understanding Learning Needs**: See what gaps modules need to address
3. **Respecting Constraints**: Design for limited time, varied access, diverse preferences
4. **Setting Realistic Scope**: Remember modules support Outcomes G, H, I, J - not full competency achievement
5. **Ensuring Inclusion**: Address the diversity of learners and their experiences of power and barriers

## Next Steps

### To Test All Personas

1. Fix YAML syntax errors in:
   - `ml_framework_personas-fundamental_stage.yaml`
   - `ml_framework_personas-stage2.yaml`
   - `ml_framework_personas-stage3.yaml`
   - `ml_framework_personas-stage4.yaml`

2. Re-run tests to validate all personas across all stages

### To Extend Testing

Consider adding tests for:

1. **Semantic Validation**: Use NLP to analyze whether competency descriptors semantically address persona gaps
2. **Testing Criteria Coverage**: Validate that module testing criteria files adequately cover all persona scenarios
3. **Learning Journey Validation**: Test that developmental trajectories align with stage progressions
4. **Barrier-Accessibility Mapping**: Ensure identified barriers have corresponding accessibility solutions

## Questions These Tests Answer

1. ✅ Do all personas have identified learning needs?
2. ✅ Do the competencies exist to address those needs?
3. ✅ Is there a competency descriptor at the right stage for each persona?
4. ✅ Is modular learning scope properly bounded?
5. ✅ Do we acknowledge that modular learning alone doesn't result in meeting competencies?
6. ✅ Are diversity and inclusion considerations documented for all personas?
7. ✅ Are learning preferences and barriers captured?
8. ✅ Do we have evidence of what personas can already demonstrate?

## Contact

For questions about these tests or to report issues, please refer to the project documentation.

---

**Last Updated:** 2025-11-17
**Test Suite Version:** 1.0
**Framework Version:** 1.0
