# Test Suites for Persona-Competency Framework

## Overview

Two comprehensive test suites validate the persona-competency framework:

1. **Persona-Competency Mapping Tests** (`test_persona_competency_mapping.py`)
   - Validates personas' learning needs map to valid competencies
   - 71 tests, all passing ✅

2. **Module Testing Criteria Tests** (`test_module_testing_criteria.py`)
   - Validates testing criteria address persona learning needs
   - 257 tests, 211 passing (82%) ⚠️

## Quick Start

```bash
# Install dependencies
pip install pytest pyyaml

# Run all tests
pytest test_persona_competency_mapping.py test_module_testing_criteria.py -v

# Run specific suite
pytest test_persona_competency_mapping.py -v  # Persona-competency tests
pytest test_module_testing_criteria.py -v     # Testing criteria tests
```

## Test Suite 1: Persona-Competency Mapping (71 tests)

### What It Tests

1. **All personas' learning needs map to valid competencies** in the framework
2. **Competencies have descriptors at appropriate stages** to address persona needs
3. **Modular learning scope is properly bounded** - provides introduction (G, H, I, J) not full competency (K)
4. **Diversity and inclusion** considerations are captured
5. **Learning readiness and accessibility** requirements are documented

### Coverage

- ✅ 71 comprehensive tests
- ✅ 5 personas tested (Stage 1)
- ✅ 27 competencies validated
- ✅ 4 modular learning outcomes verified (G, H, I, J)
- ✅ Diversity profiles, learning barriers, and accessibility needs checked

### Status

**✅ All 71 tests passing**

### Documentation

See `TEST_DOCUMENTATION.md` for detailed information.

## Test Suite 2: Module Testing Criteria (257 tests)

### What It Tests

1. **Testing criteria completeness** - All 25 personas have evaluation questions
2. **Testing scenarios** - Map to valid competencies with meaningful questions
3. **Learning needs alignment** - Scenarios address personas' target competencies
4. **Modular learning scope** - Criteria respect realistic boundaries
5. **Cross-cutting themes** - 8 required themes present and comprehensive
6. **Accessibility** - Personas with disabilities have accessibility questions
7. **Competency coverage** - Scenarios collectively test diverse competencies

### Coverage

- 257 comprehensive tests
- 25 personas across all 5 stages
- 27 competencies validated
- 8 cross-cutting themes verified
- 13/27 competencies currently tested in scenarios (48%)
- 13/25 personas have testing scenarios (52%)

### Status

**⚠️ 211/257 tests passing (82%), 40 skipped, 6 failed**

### Issues Identified

1. **5 Invalid competency references** (Personas 21-25) - Scenarios reference paraphrased names instead of exact competency names
2. **1 Missing accessibility questions** (Persona 13) - Has disability but no accessibility evaluation questions
3. **12 Personas without scenarios** (4 from Stage 1, 11 from Stage 2)
4. **14 Untested competencies** - No scenarios for nearly half the competencies

### Documentation

See `TEST_DOCUMENTATION_MODULE_CRITERIA.md` for detailed analysis and recommendations.

## Key Files

### Test Files
- `test_persona_competency_mapping.py` - Persona-competency mapping tests
- `test_module_testing_criteria.py` - Testing criteria validation tests

### Documentation
- `TEST_DOCUMENTATION.md` - Persona-competency test documentation
- `TEST_DOCUMENTATION_MODULE_CRITERIA.md` - Testing criteria test documentation
- `README_TESTS.md` - This file (overview)

### Framework Files
- `ml_framework_standards-competencies-v1_0.yaml` - 27 competencies across 5 stages
- `ml_modular_logic_model-v1_0.yaml` - Logic model (scope boundaries)
- `ml_framework_personas-*.yaml` - Personas by stage (5 files)
- `ml_framework_module_testing_criteria-*.yaml` - Testing criteria by stage (5 files)

## Critical Insight: Modular Learning Scope

Both test suites validate that we maintain **realistic expectations** about modular learning:

**✅ Modular learning DOES:**
- Build awareness and credibility (Outcome G)
- Engage learners in inquiry and reflection (Outcome H)
- Provide foundational knowledge (Outcome I)
- Help learners recognize further development needs (Outcome J)

**❌ Modular learning alone does NOT:**
- Result in fully meeting competencies (Outcome K)
- Replace deeper learning, workplace application, or formal assessment
- Eliminate the need for signposting to additional resources

This boundary is validated in:
- Logic model scope (in/out of scope markers)
- Persona misunderstandings that modules should address
- Cross-cutting theme "Acknowledgment of Limitations"
- Evaluation questions avoiding unrealistic scope expectations

## How Test Suites Work Together

| Persona-Competency Tests | Testing Criteria Tests |
|-------------------------|------------------------|
| Personas → competencies | Testing criteria → competencies |
| Learning needs identified | Testing criteria address needs |
| Competency framework complete | Scenarios reference valid competencies |
| Modular learning scope (logic model) | Criteria respect realistic scope |
| Diversity profiles exist | Questions address diversity |

**Together:** Ensure personas have valid needs AND testing criteria exist to evaluate whether modules address those needs ✅

## Current Status Summary

```
Persona-Competency Tests:     71/71 passing (100%) ✅
Testing Criteria Tests:        211/257 passing (82%) ⚠️
                               ───────
Combined:                      282/328 tests (86%)
```

## Recommendations

### Immediate (Fix Test Failures)

1. Fix 5 invalid competency references in Personas 21-25
2. Add accessibility questions for Persona 13
3. Fix YAML syntax errors in persona files to enable 40 skipped tests

### Short-Term (Complete Coverage)

4. Add testing scenarios for 4 Stage 1 personas without scenarios
5. Add testing scenarios for all 11 Stage 2 personas

### Long-Term (Expand Coverage)

6. Ensure all 27 competencies are tested across persona set
7. Review diversity barrier coverage in evaluation questions
8. Consider adding semantic validation of question-need alignment

## Notes

- Some persona files (Fundamental, Stage 2, 3, 4) have YAML parsing errors
- This causes 40 tests to be skipped (can't validate alignment without persona data)
- Fix YAML syntax to enable full validation across all stages
