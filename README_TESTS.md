# Persona-Competency Tests

## Quick Start

```bash
# Install dependencies
pip install pytest pyyaml

# Run all tests
pytest test_persona_competency_mapping.py -v

# Expected result: 71 tests passing
```

## What These Tests Do

These tests validate that:

1. **All personas' learning needs map to valid competencies** in the framework
2. **Competencies have descriptors at appropriate stages** to address persona needs
3. **Modular learning scope is properly bounded** - it provides introduction and awareness (Outcomes G, H, I, J) but does NOT alone result in meeting competencies (Outcome K)
4. **Diversity and inclusion** considerations are captured for all personas
5. **Learning readiness and accessibility** requirements are documented

## Test Coverage

- ✅ 71 comprehensive tests
- ✅ 5 personas tested (Stage 1)
- ✅ 27 competencies validated
- ✅ 4 modular learning outcomes verified (G, H, I, J)
- ✅ Diversity profiles, learning barriers, and accessibility needs checked

## Key Files

- `test_persona_competency_mapping.py` - Main test suite
- `TEST_DOCUMENTATION.md` - Detailed documentation
- `ml_framework_standards-competencies-v1_0.yaml` - Competencies framework
- `ml_modular_logic_model-v1_0.yaml` - Logic model (scope boundaries)
- `ml_framework_personas-stage1.yaml` - Personas (Stage 1)

## Critical Insight

These tests ensure we maintain **realistic expectations** about modular learning:

**✅ Modular learning DOES:**
- Build awareness and credibility (Outcome G)
- Engage learners in inquiry and reflection (Outcome H)
- Provide foundational knowledge (Outcome I)
- Help learners recognize further development needs (Outcome J)

**❌ Modular learning alone does NOT:**
- Result in fully meeting competencies (Outcome K)
- Replace deeper learning, workplace application, or formal assessment
- Eliminate the need for signposting to additional resources

## Documentation

See `TEST_DOCUMENTATION.md` for:
- Detailed test descriptions
- Test suite breakdowns
- Running specific test suites
- Interpreting results
- Next steps and extensions

## Current Status

**✅ All 71 tests passing**

Note: Some persona files (Fundamental, Stage 2, 3, 4) have YAML parsing errors and are not yet tested. Fix YAML syntax to enable testing of all personas across all stages.
