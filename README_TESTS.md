# Test Suites for Persona-Competency Framework

## Overview

Two comprehensive test suites validate the persona-competency framework:

1. **Persona-Competency Mapping Tests** (`test_persona_competency_mapping.py`)
   - Validates personas' learning needs map to valid competencies
   - 331 tests, all passing (100%) ✅

2. **Module Testing Criteria Tests** (`test_module_testing_criteria.py`)
   - Validates testing criteria address persona learning needs
   - 257 tests, all passing (100%) ✅

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
- **27/27 competencies tested in scenarios (100%)** ✅
- **25/25 personas have testing scenarios (100%)** ✅

### Status

**✅ 257/257 tests passing (100%)**

### Achievements

1. **✅ All 27 competencies tested** - 100% competency coverage achieved
2. **✅ All 25 personas have 3 testing scenarios** - 75 scenarios total
3. **✅ All accessibility questions addressed** - All personas with disabilities have accessibility evaluation questions
4. **✅ All competency references valid** - All scenarios use exact names from framework
5. **✅ 45 new scenarios added** - Stage 1 (12 scenarios) + Stage 2 (33 scenarios)

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
Persona-Competency Tests:     331/331 passing (100%) ✅
Testing Criteria Tests:        257/257 passing (100%) ✅
                               ───────
Combined:                      588/588 tests (100%) ✅
```

## Completed Achievements

### ✅ Full Competency Coverage (100%)
All 27 competencies now tested across the persona set through strategic scenario design

### ✅ Complete Persona Scenarios (100%)
All 25 personas (Fundamental through Stage 4) have 3 testing scenarios each = 75 total scenarios

### ✅ All Issues Resolved
- Fixed YAML syntax errors in 3 persona files (stages 2-4)
- Fixed 31 invalid competency references across all stages
- Added accessibility questions for Persona 13
- Added 45 new scenarios (Stage 1: 12, Stage 2: 33)
- Achieved 100% competency coverage
- Achieved 100% test pass rate (588/588 tests)

## Scenario Highlights

**Stage 1 (4 personas, 12 scenarios):**
- Persona 6 (Midwife): Maternal health inequalities, relationship building, personalized care
- Persona 7 (Community Pharmacist): Team engagement, collaborative leadership, workplace safety
- Persona 8 (Ward Nurse): Managing upwards, international staff experience, cross-cultural communication
- Persona 9 (Estates Manager): Data-driven decisions, personal productivity, technical leadership

**Stage 2 (11 personas, 33 scenarios):**
- Complete coverage of middle management competencies
- Addresses ageism, neurodivergence, disability, religious discrimination, migration experiences
- Tests resource allocation, governance, performance management, innovation

## Future Enhancements

1. Add semantic validation of question-need alignment using NLP
2. Create competency-specific testing guidance
3. Develop persona journey mapping across stages
