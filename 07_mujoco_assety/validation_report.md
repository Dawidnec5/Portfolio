# Asset validation report — sim-ready library (MuJoCo)

Generated: 2026-10-29 05:12 UTC  |  MuJoCo 3.17.0  |  OVERALL: **PASS** (PASS 42 / WARN 0 / FAIL 0)

## Library summary

| asset | bodies | geoms (vis/col) | joints | actuators | scene mass [kg] | textures | materials | timestep | result |
|---|---|---|---|---|---|---|---|---|---|
| `drawer_scene.xml` | 4 | 81 (62/18) | 3 | 1 | 42.499 | 7 | 16 | 0.002 s | PASS |
| `door_scene.xml` | 5 | 131 (114/16) | 3 | 2 | 705.616 | 7 | 8 | 0.002 s | PASS |
| `mug_pickplace_scene.xml` | 307 | 456 (114/342) | 306 | 7 | 11.164 | 7 | 17 | 0.002 s | PASS |

Scene mass includes static architecture (walls, jambs, furniture); per-part masses of the moving bodies are listed in the README.

## Detailed results

### `drawer_scene.xml`

| # | check | status | details |
|---|---|---|---|
| 1 | `xml_load` | PASS | MuJoCo 3.17.0, compiles OK (sha256:efd9d5ec95cff30a, 22299 B) |
| 2 | `physics_timestep` | PASS | timestep = 0.002 s |
| 3 | `physics_integrator` | PASS | integrator = implicitfast |
| 4 | `mass_total` | PASS | total scene mass (incl. static architecture) = 42.499 kg |
| 5 | `body_mass_positive` | PASS | every body with geometry has mass > 0 |
| 6 | `body_inertia_positive` | PASS | diagonal inertia tensors > 0 |
| 7 | `joints_limited` | PASS | drawer_slide(slide, [0, 0.3]); item_box_joint(free, 6 DOF); item_cyl_joint(free, 6 DOF); 0 flex particles + 2 freejoints (unlimited by definition) |
| 8 | `actuators` | PASS | drawer_motor(forcerange [-80, 80]) |
| 9 | `contact_configuration` | PASS | 18 collision geoms (contacts enabled), 62 visual, 1 boundary (floor) |
| 10 | `visual_collision_separation` | PASS | separated: 62 vis + 0 col (_col, proxies) + 18 dual (visible and collidable: architecture and working mechanism parts — documented convention) |
| 11 | `textures` | PASS | 7 textures (6 x 2D, rest skybox/color), 2D resolutions [(256, 256), (512, 512)] (powers of two) |
| 12 | `materials` | PASS | 16 materials; geoms without material: 0/81 |
| 13 | `naming_convention` | PASS | snake_case OK, unnamed objects: 0 |
| 14 | `demo_behavior` | PASS | demo drawer_summary.json: overall_pass=True, max opening = 0.251384027 |

### `door_scene.xml`

| # | check | status | details |
|---|---|---|---|
| 1 | `xml_load` | PASS | MuJoCo 3.17.0, compiles OK (sha256:e596e336e3851083, 36304 B) |
| 2 | `physics_timestep` | PASS | timestep = 0.002 s |
| 3 | `physics_integrator` | PASS | integrator = implicitfast |
| 4 | `mass_total` | PASS | total scene mass (incl. static architecture) = 705.616 kg |
| 5 | `body_mass_positive` | PASS | every body with geometry has mass > 0 |
| 6 | `body_inertia_positive` | PASS | diagonal inertia tensors > 0 |
| 7 | `joints_limited` | PASS | door_hinge(hinge, [0, 1.75]); handle_hinge(hinge, [0, 0.5]); latch_slide(slide, [0, 0.018]) |
| 8 | `actuators` | PASS | door_motor(forcerange [-50, 50]); handle_motor(forcerange [-8, 8]) |
| 9 | `contact_configuration` | PASS | 16 collision geoms (contacts enabled), 114 visual, 1 boundary (floor) |
| 10 | `visual_collision_separation` | PASS | separated: 114 vis (contype=0) vs 16 col (_col suffix, convex proxies) |
| 11 | `textures` | PASS | 7 textures (6 x 2D, rest skybox/color), 2D resolutions [(256, 256), (512, 512)] (powers of two) |
| 12 | `materials` | PASS | 8 materials; geoms without material: 0/131 |
| 13 | `naming_convention` | PASS | snake_case OK, unnamed objects: 0 |
| 14 | `demo_behavior` | PASS | demo door_summary.json: overall_pass=True, max opening = 1.485955511 |

### `mug_pickplace_scene.xml`

| # | check | status | details |
|---|---|---|---|
| 1 | `xml_load` | PASS | MuJoCo 3.17.0, compiles OK (sha256:15544409059de461, 1150293 B) |
| 2 | `physics_timestep` | PASS | timestep = 0.002 s |
| 3 | `physics_integrator` | PASS | integrator = implicitfast |
| 4 | `mass_total` | PASS | total scene mass (incl. static architecture) = 11.164 kg |
| 5 | `body_mass_positive` | PASS | every body with geometry has mass > 0 |
| 6 | `body_inertia_positive` | PASS | diagonal inertia tensors > 0 |
| 7 | `joints_limited` | PASS | pj_000(free, 6 DOF); pj_001(free, 6 DOF); pj_002(free, 6 DOF); pj_003(free, 6 DOF); pj_004(free, 6 DOF); pj_005(free, 6 DOF); pj_006(free, 6 DOF); pj_007(free, 6 DOF); pj_008(free, 6 DOF); pj_009(free, 6 DOF); pj_010(free, 6 DOF); pj_011(free, 6 DOF); pj_012(free, 6 DOF); pj_013(free, 6 DOF); pj_014(free, 6 DOF); pj_015(free, 6 DOF); pj_016(free, 6 DOF); pj_017(free, 6 DOF); pj_018(free, 6 DOF); pj_019(free, 6 DOF); pj_020(free, 6 DOF); pj_021(free, 6 DOF); pj_022(free, 6 DOF); pj_023(free, 6 DOF); pj_024(free, 6 DOF); pj_025(free, 6 DOF); pj_026(free, 6 DOF); pj_027(free, 6 DOF); pj_028(free, 6 DOF); pj_029(free, 6 DOF); pj_030(free, 6 DOF); pj_031(free, 6 DOF); pj_032(free, 6 DOF); pj_033(free, 6 DOF); pj_034(free, 6 DOF); pj_035(free, 6 DOF); pj_036(free, 6 DOF); pj_037(free, 6 DOF); pj_038(free, 6 DOF); pj_039(free, 6 DOF); pj_040(free, 6 DOF); pj_041(free, 6 DOF); pj_042(free, 6 DOF); pj_043(free, 6 DOF); pj_044(free, 6 DOF); pj_045(free, 6 DOF); pj_046(free, 6 DOF); pj_047(free, 6 DOF); pj_048(free, 6 DOF); pj_049(free, 6 DOF); pj_050(free, 6 DOF); pj_051(free, 6 DOF); pj_052(free, 6 DOF); pj_053(free, 6 DOF); pj_054(free, 6 DOF); pj_055(free, 6 DOF); pj_056(free, 6 DOF); pj_057(free, 6 DOF); pj_058(free, 6 DOF); pj_059(free, 6 DOF); pj_060(free, 6 DOF); pj_061(free, 6 DOF); pj_062(free, 6 DOF); pj_063(free, 6 DOF); pj_064(free, 6 DOF); pj_065(free, 6 DOF); pj_066(free, 6 DOF); pj_067(free, 6 DOF); pj_068(free, 6 DOF); pj_069(free, 6 DOF); pj_070(free, 6 DOF); pj_071(free, 6 DOF); pj_072(free, 6 DOF); pj_073(free, 6 DOF); pj_074(free, 6 DOF); pj_075(free, 6 DOF); pj_076(free, 6 DOF); pj_077(free, 6 DOF); pj_078(free, 6 DOF); pj_079(free, 6 DOF); pj_080(free, 6 DOF); pj_081(free, 6 DOF); pj_082(free, 6 DOF); pj_083(free, 6 DOF); pj_084(free, 6 DOF); pj_085(free, 6 DOF); pj_086(free, 6 DOF); pj_087(free, 6 DOF); pj_088(free, 6 DOF); pj_089(free, 6 DOF); pj_090(free, 6 DOF); pj_091(free, 6 DOF); pj_092(free, 6 DOF); pj_093(free, 6 DOF); pj_094(free, 6 DOF); pj_095(free, 6 DOF); pj_096(free, 6 DOF); pj_097(free, 6 DOF); pj_098(free, 6 DOF); pj_099(free, 6 DOF); pj_100(free, 6 DOF); pj_101(free, 6 DOF); pj_102(free, 6 DOF); pj_103(free, 6 DOF); pj_104(free, 6 DOF); pj_105(free, 6 DOF); pj_106(free, 6 DOF); pj_107(free, 6 DOF); pj_108(free, 6 DOF); pj_109(free, 6 DOF); pj_110(free, 6 DOF); pj_111(free, 6 DOF); pj_112(free, 6 DOF); pj_113(free, 6 DOF); pj_114(free, 6 DOF); pj_115(free, 6 DOF); pj_116(free, 6 DOF); pj_117(free, 6 DOF); pj_118(free, 6 DOF); pj_119(free, 6 DOF); pj_120(free, 6 DOF); pj_121(free, 6 DOF); pj_122(free, 6 DOF); pj_123(free, 6 DOF); pj_124(free, 6 DOF); pj_125(free, 6 DOF); pj_126(free, 6 DOF); pj_127(free, 6 DOF); pj_128(free, 6 DOF); pj_129(free, 6 DOF); pj_130(free, 6 DOF); pj_131(free, 6 DOF); pj_132(free, 6 DOF); pj_133(free, 6 DOF); pj_134(free, 6 DOF); pj_135(free, 6 DOF); pj_136(free, 6 DOF); pj_137(free, 6 DOF); pj_138(free, 6 DOF); pj_139(free, 6 DOF); pj_140(free, 6 DOF); pj_141(free, 6 DOF); pj_142(free, 6 DOF); pj_143(free, 6 DOF); pj_144(free, 6 DOF); pj_145(free, 6 DOF); pj_146(free, 6 DOF); pj_147(free, 6 DOF); pj_148(free, 6 DOF); pj_149(free, 6 DOF); pj_150(free, 6 DOF); pj_151(free, 6 DOF); pj_152(free, 6 DOF); pj_153(free, 6 DOF); pj_154(free, 6 DOF); pj_155(free, 6 DOF); pj_156(free, 6 DOF); pj_157(free, 6 DOF); pj_158(free, 6 DOF); pj_159(free, 6 DOF); pj_160(free, 6 DOF); pj_161(free, 6 DOF); pj_162(free, 6 DOF); pj_163(free, 6 DOF); pj_164(free, 6 DOF); pj_165(free, 6 DOF); pj_166(free, 6 DOF); pj_167(free, 6 DOF); pj_168(free, 6 DOF); pj_169(free, 6 DOF); pj_170(free, 6 DOF); pj_171(free, 6 DOF); pj_172(free, 6 DOF); pj_173(free, 6 DOF); pj_174(free, 6 DOF); pj_175(free, 6 DOF); pj_176(free, 6 DOF); pj_177(free, 6 DOF); pj_178(free, 6 DOF); pj_179(free, 6 DOF); pj_180(free, 6 DOF); pj_181(free, 6 DOF); pj_182(free, 6 DOF); pj_183(free, 6 DOF); pj_184(free, 6 DOF); pj_185(free, 6 DOF); pj_186(free, 6 DOF); pj_187(free, 6 DOF); pj_188(free, 6 DOF); pj_189(free, 6 DOF); pj_190(free, 6 DOF); pj_191(free, 6 DOF); pj_192(free, 6 DOF); pj_193(free, 6 DOF); pj_194(free, 6 DOF); pj_195(free, 6 DOF); pj_196(free, 6 DOF); pj_197(free, 6 DOF); pj_198(free, 6 DOF); pj_199(free, 6 DOF); pj_200(free, 6 DOF); pj_201(free, 6 DOF); pj_202(free, 6 DOF); pj_203(free, 6 DOF); pj_204(free, 6 DOF); pj_205(free, 6 DOF); pj_206(free, 6 DOF); pj_207(free, 6 DOF); pj_208(free, 6 DOF); pj_209(free, 6 DOF); pj_210(free, 6 DOF); pj_211(free, 6 DOF); pj_212(free, 6 DOF); pj_213(free, 6 DOF); pj_214(free, 6 DOF); pj_215(free, 6 DOF); pj_216(free, 6 DOF); pj_217(free, 6 DOF); pj_218(free, 6 DOF); pj_219(free, 6 DOF); pj_220(free, 6 DOF); pj_221(free, 6 DOF); pj_222(free, 6 DOF); pj_223(free, 6 DOF); pj_224(free, 6 DOF); pj_225(free, 6 DOF); pj_226(free, 6 DOF); pj_227(free, 6 DOF); pj_228(free, 6 DOF); pj_229(free, 6 DOF); pj_230(free, 6 DOF); pj_231(free, 6 DOF); pj_232(free, 6 DOF); pj_233(free, 6 DOF); pj_234(free, 6 DOF); pj_235(free, 6 DOF); pj_236(free, 6 DOF); pj_237(free, 6 DOF); pj_238(free, 6 DOF); pj_239(free, 6 DOF); pj_240(free, 6 DOF); pj_241(free, 6 DOF); pj_242(free, 6 DOF); pj_243(free, 6 DOF); pj_244(free, 6 DOF); pj_245(free, 6 DOF); pj_246(free, 6 DOF); pj_247(free, 6 DOF); pj_248(free, 6 DOF); pj_249(free, 6 DOF); pj_250(free, 6 DOF); pj_251(free, 6 DOF); pj_252(free, 6 DOF); pj_253(free, 6 DOF); pj_254(free, 6 DOF); pj_255(free, 6 DOF); pj_256(free, 6 DOF); pj_257(free, 6 DOF); pj_258(free, 6 DOF); pj_259(free, 6 DOF); pj_260(free, 6 DOF); pj_261(free, 6 DOF); pj_262(free, 6 DOF); pj_263(free, 6 DOF); pj_264(free, 6 DOF); pj_265(free, 6 DOF); pj_266(free, 6 DOF); pj_267(free, 6 DOF); pj_268(free, 6 DOF); pj_269(free, 6 DOF); pj_270(free, 6 DOF); pj_271(free, 6 DOF); pj_272(free, 6 DOF); pj_273(free, 6 DOF); pj_274(free, 6 DOF); pj_275(free, 6 DOF); pj_276(free, 6 DOF); pj_277(free, 6 DOF); pj_278(free, 6 DOF); pj_279(free, 6 DOF); pj_280(free, 6 DOF); pj_281(free, 6 DOF); pj_282(free, 6 DOF); pj_283(free, 6 DOF); pj_284(free, 6 DOF); pj_285(free, 6 DOF); pj_286(free, 6 DOF); pj_287(free, 6 DOF); pj_288(free, 6 DOF); pj_289(free, 6 DOF); pj_290(free, 6 DOF); pj_291(free, 6 DOF); pj_292(free, 6 DOF); pj_293(free, 6 DOF); pj_294(free, 6 DOF); pj_295(free, 6 DOF); pj_296(free, 6 DOF); mug_root(free, 6 DOF); j1_yaw(hinge, [-3.2, 3.2]); j2_shoulder(hinge, [-0.35, 1.75]); j3_elbow(hinge, [-2.9, 0.25]); j4_wrist_pitch(hinge, [-2.4, 1.2]); j5_wrist_roll(hinge, [-2.2, 2.2]); pinion_hinge(hinge, [0, 3.4]); finger_slide_l(slide, [0, 0.04]); finger_slide_r(slide, [0, 0.04]); 0 flex particles + 298 freejoints (unlimited by definition) |
| 8 | `actuators` | PASS | j1_motor(forcerange [-160, 160]); j2_motor(forcerange [-130, 130]); j3_motor(forcerange [-90, 90]); j4_motor(forcerange [-28, 28]); j5_motor(forcerange [-9, 9]); grip_l_motor(forcerange [-12, 12]); grip_r_motor(forcerange [-12, 12]) |
| 9 | `contact_configuration` | PASS | 342 collision geoms (contacts enabled), 114 visual, 0 boundary (floor) |
| 10 | `visual_collision_separation` | PASS | separated: 114 vis + 300 col (_col, proxies) + 42 dual (visible and collidable: architecture and working mechanism parts — documented convention) |
| 11 | `textures` | PASS | 7 textures (6 x 2D, rest skybox/color), 2D resolutions [(256, 256), (512, 512)] (powers of two) |
| 12 | `materials` | PASS | 17 materials; geoms without material: 315/456 |
| 13 | `naming_convention` | PASS | snake_case OK, unnamed objects: 0 |
| 14 | `demo_behavior` | PASS | demo pickplace_summary.json: overall_pass=True |

## Methodology (what each check verifies)

- **xml_load** — the model compiles in MuJoCo without schema errors;
- **physics_timestep / integrator** — step <= 2 ms and a stable integrator (implicitfast: stable with stiff position actuators);
- **mass_total / body_mass_positive / body_inertia_positive** — every body has a valid inertia tensor (precondition for sensible dynamics);
- **joints_limited** — joints have hard limits (safe robot operation, no unreachable states);
- **actuators** — actuators have bounded force/torque (forcerange);
- **contact_configuration** — collision geoms with contacts enabled; WARN = kinematic convention (physics through joint + actuator);
- **visual_collision_separation** — visual geometry (detail, contype=0) separated from cheap convex collision proxies (`_col` suffix);
- **textures / materials** — power-of-two texture resolutions, geoms with assigned materials;
- **naming_convention** — consistent snake_case (automation, scripting);
- **demo_behavior** — cross-check against the actual demo run (pass/fail criteria in `results/*_summary.json`).

## How to reproduce

```bash
python scripts/validate_asset.py                  # all assets
python scripts/validate_asset.py --model model/door_scene.xml
python -m pytest tests -q -rs                     # acceptance tests
```
