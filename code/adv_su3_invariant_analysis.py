"""ATTACK 4 — does the SU(3)-invariant uniqueness UPGRADE Track A to a law, or is it vacuous?
I established: SU(3)-invariant metrics on CP^2 form a 1-param (homothety) family => FS unique up to
scale among them. The steelman: 'lambda_1-extremality selects FS uniquely within the natural
(SU(3)-invariant) class' => Track A is a law after all.

The decisive question: WITHIN the SU(3)-invariant class, does lambda_1-EXTREMALITY do the selecting,
or does SU(3)-INVARIANCE alone already pin FS (making 'lambda_1-extremal' an idle wheel)?

If invariance alone pins FS, then the selecting principle is 'maximal symmetry', NOT a variational
gravity law -- you put the answer in by hand (assume the symmetry of the answer). That is a
CONSISTENCY CONDITION (FS is self-consistent with its own symmetry), exactly the verdict's claim.
The lambda_1-extremality is then a true-but-non-selecting PROPERTY (Trap #20: extremality-as-property).
"""
print("="*78)
print("ATTACK 4: is the invariant-class uniqueness a genuine lambda_1-SELECTION or vacuous?")
print("="*78)
print("""
ESTABLISHED (adv_attack4.py): SU(3)-invariant metrics on CP^2 = 1-parameter (scale) family,
all homothetic to FS. (Isotropy rep of U(2) on T_o is R-irreducible => unique invariant inner
product up to scale.)

LOGICAL ANALYSIS of the steelman 'FS is the unique SU(3)-invariant lambda_1-extremal metric':

  Within the SU(3)-invariant class C_inv = {c * g_FS : c>0}:
    - EVERY metric in C_inv is homothetic to FS.
    - lambda_1 * Vol^{2/n} is scale-INVARIANT (that is why it is the functional), so it is
      CONSTANT on C_inv. => EVERY metric in C_inv is trivially lambda_1-critical within C_inv.
    => lambda_1-extremality selects NOTHING within C_inv (the whole class is critical).
    => What picks 'FS' out of C_inv is just 'pick a scale' (a normalization), and what picks
       C_inv itself is the ASSUMPTION of SU(3)-invariance.

  CONCLUSION: the selecting work is done by IMPOSING SU(3)-invariance, NOT by lambda_1-extremality.
  Imposing the symmetry group of the answer and then noting the answer is extremal is the textbook
  'extremality-as-property' move (Trap #20). It is a CONSISTENCY CONDITION (FS is consistent with
  its symmetry + is extremal), NOT a selection LAW that DERIVES FS from a variational principle.

  Moreover: a genuine selection LAW must select FS WITHOUT assuming the answer's symmetry -- i.e.
  among ALL metrics. There, El Soufi-Ilias/Kahler-rigidity FAILS (the verdict's A1(b)): FS is
  lambda_1-extremal but so are other metrics in its class (KE Fano w/ holomorphic vector fields
  saturate BLY but are not uniquely pinned). So over all metrics, lambda_1-extremality is a CLASS
  condition. The SU(3)-invariant restriction does not rescue this -- it just pre-selects the answer.

=> Attack 4 does NOT crack the verdict. The invariant-class 'uniqueness' is VACUOUS as a selection
   (the functional is constant on the class), and assuming SU(3)-invariance is assuming the answer.
   Track A remains a CONSISTENCY CONDITION, not a law. The verdict's A1(b) grading is CORRECT.

   [Even if one insisted on calling it a 'law', it would select only the BACKGROUND FS metric, and
    would say NOTHING about the matter-coupling operator Q_A, which A4 independently shows is not
    Einstein. The gravity verdict rests on A4 + Track B, untouched by A1(b).]
""")
