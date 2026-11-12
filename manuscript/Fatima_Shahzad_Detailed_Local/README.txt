Fatima Shahzad — detailed N-body manuscript

Contents:
  main.tex       Updated two-column LaTeX manuscript
  figures/       Complete unsplit PNG figures referenced by main.tex
  main.pdf       Locally compiled preview

Windows PowerShell / MiKTeX:
  1. Extract this ZIP anywhere, preferably inside your fatima project folder.
  2. Open PowerShell inside Fatima_Shahzad_Detailed_Local.
  3. Run:
     latexmk -pdf -interaction=nonstopmode -file-line-error -halt-on-error main.tex
  4. Open main.pdf.

Changes:
- Author: Fatima Shahzad
- Accessible introduction from first principles
- Thorough mathematical framework deriving/explaining physical states, gravity,
  two-body circular control, restricted three-body dynamics, Euler, leapfrog,
  RK4, adaptive tolerance, convergence, tangent equations, FTLE, Jacobi constant,
  and state/FTLE accuracy criteria
- Compact section headings, vertical spacing, anchored original unsplit plots

This manuscript is a writing/layout revision, not an independent numerical audit.
Check all experimental claims against primary notebooks and CSV outputs before submission.
