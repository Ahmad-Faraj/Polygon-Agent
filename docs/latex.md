# Polygon LaTeX Rules

> **PRIMARY SOURCE**: docs/statements-tex-manual.md
> Read the full official manual before writing any statement file.
> This file provides quick examples; the manual is authoritative.

Reference: https://polygon.codeforces.com/docs/statements-tex-manual
Polygon renders its own LaTeX dialect. Violations cause compile errors or broken PDF.

---

## Math mode -- ALL variables MUST be in math mode

  CORRECT: $n$  $a_i$  $k$  $W$  $O(n \log n)$
  WRONG:   n    a_i    k    W    plain text

  Inline:  $...$
  Display: \[ ... \]

---

## Symbols -- use ONLY these forms

  \leq     not <=      $a \leq b$
  \geq     not >=      $a \geq b$
  \neq     not !=      $i \neq j$
  \times   not x or *  $n \times m$
  \ldots   not ...     $a_1, a_2, \ldots, a_n$
  \cdots   in sums     $a_1 + a_2 + \cdots + a_n$
  \longrightarrow      $3 \longrightarrow 12$
  \blacksquare         section marker
  \lfloor x \rfloor   floor
  \lceil x \rceil    ceiling
  a_i   a_{ij}   a_{10}    subscripts
  10^5  n^2      2^{10}    superscripts
  \text{target}         text inside math mode

---

## Constraint format -- use exactly this style

  $(1 \leq n \leq 2 \times 10^5)$
  $(0 \leq L \leq S \leq 400)$
  $(-10^9 \leq a_i \leq 10^9)$

  Em-dash between description and constraint:
  The first line contains $n$ $(1 \leq n \leq 10^5)$ --- the number of elements.

---

## Text formatting

  \textbf{bold}   or   \bf{bold}
  \textit{italic}
  \texttt{monospace}
  \large{bigger text}
  \t{YES}   \t{NO}   \t{-1}   \t{-1 -1}   (literal tokens, fixed-width)

---

## Environments -- all valid in Polygon

  \begin{itemize}
    \item First point.
    \item Second point.
  \end{itemize}

  \begin{enumerate}
    \item Step one.
    \item Step two.
  \end{enumerate}

  \begin{center}
    Centered content.
  \end{center}

---

## Real example from a valid Polygon problem (Snakes and Ladders)

legend.tex:
  $Faraj$ likes playing Snakes and Ladders with special rules.
  Given a grid $A$ of size $n \times m$. You start at \bf{(1,1)}.
  Your goal is to reach \bf{(n,m)}.

  \begin{itemize}
    \item There is a Ladder between cells \bf{(3 $\longrightarrow$ 12)}.
    \item There is a Snake between cells \bf{(9 $\longrightarrow$ 8)}.
  \end{itemize}

  $\cdots$

  $\blacksquare$ \large{Take the following Example:}

  \begin{enumerate}
    \item We start at \bf{(1)}. Choose wheel value \bf{{1}} and move forward.
    \item We are at \bf{(4)}. This cell has a Ladder.
  \end{enumerate}

input.tex:
  First line contains $t$ $(1 \leq t \leq 10)$.
  Next $t$ test cases each have two lines:
  Line 1: $n$ and $m$ $(2 \leq n \leq m \leq 20)$ --- rows and columns.
  Line 2: $L$ and $S$ $(0 \leq L \leq S \leq 400)$ --- ladders and snakes.
  It is guaranteed that $n$ is an \bf{odd} number.

notes.tex:
  In the first example, the grid is $3 \times 4$.
  We finished with the minimum of \bf{4 spins}.

tutorial.tex:
  \textbf{Key Observations}
  \begin{enumerate}
      \item The wheel cycles through $\{1, 2, 3\}$ and resets.
      \item Using a ladder or snake does not advance the wheel pointer.
  \end{enumerate}
  \textbf{Solution Approach}
  Run BFS on state $(cell, wheel\_pos, ladder\_used, snake\_used)$.
  \textbf{Complexity Analysis}
  \begin{itemize}
      \item \textbf{Time}: $O(n \times m)$ --- BFS visits each state once.
      \item \textbf{Space}: $O(n \times m)$.
  \end{itemize}

---

## FORBIDDEN -- causes compile error on Polygon

  \usepackage{...}       Polygon manages packages -- remove entirely
  \begin{document}       Polygon wraps this -- remove entirely
  \documentclass{...}    remove entirely
  \newcommand{...}       no custom macros
  \section{...}          use \textbf{} for headings
  \begin{verbatim}       use \texttt{} or \t{}

---

## Common hallucinations to fix before lint

  <= >=  in text             use \leq  \geq
  ...    in text             use \ldots
  x      for multiply        use \times
  plain n outside $          use $n$
  \begin{document}        remove
  \usepackage{amsmath}    remove
  double backslash mid-text  only valid in tabular/align