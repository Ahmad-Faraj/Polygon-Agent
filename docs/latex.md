# Polygon LaTeX Rules

Polygon uses a strict subset of LaTeX. Violations cause compile errors.
Reference: https://polygon.codeforces.com/docs/statements-tex-manual

## Math mode -- ALL variables MUST be in math mode

  CORRECT: dollar-n-dollar, dollar-a_i-dollar
  WRONG:   plain n, plain a_i

  Inline math: dollar...dollar
  Display math: \[  ...  \]

## Required symbols (backslash versions only)

  \leq       not <=
  \geq       not >=
  \neq       not !=
  \times     not x or *
  \ldots     not ...
  \lfloor x \rfloor   floor function
  \lceil x \rceil    ceiling function
  a_i, a_{ij}   subscripts
  10^5, n^2     superscripts
  \text{target}  text inside math mode

## Constraint format

  ( \leq n \leq 2 \times 10^5$,  \leq a_i \leq 10^9$)

  Use --- (three dashes) for em-dash:
  The first line contains $ ( \leq n \leq 10^5$) --- the number of elements.

## Token display (Polygon-specific \t command)

  \t{YES}   \t{NO}   \t{-1 -1}
  Print \t{YES} if possible, \t{NO} otherwise.

## Text formatting

  \textbf{bold}   \textit{italic}   \texttt{monospace}

## Lists

  \begin{itemize}
      \item First point.
      \item Second point.
  \end{itemize}

  \begin{enumerate}
      \item Step one.
      \item Step two.
  \end{enumerate}

## FORBIDDEN -- causes compile error on Polygon

  \usepackage{...}       Polygon manages packages -- remove entirely
  \begin{document}       Polygon wraps this -- remove entirely
  \documentclass{...}    same -- remove entirely
  \newcommand{...}       no custom macros
  \section{...}          use \textbf{} for headings instead
  \begin{verbatim}       use \texttt{} or \t{} instead

## Tutorial structure (ECPC mandatory)

  \textbf{Key Observations}
  \begin{enumerate}
      \item Observation with proof if non-obvious.
  \end{enumerate}

  \textbf{Solution Approach}

  Step-by-step algorithm.

  \textbf{Complexity Analysis}
  \begin{itemize}
      \item \textbf{Time}: (n \log n)$ --- reason.
      \item \textbf{Space}: (n)$ --- reason.
  \end{itemize}

## Common hallucinations to avoid

  \begin{document}         remove
  \usepackage{amsmath}      remove
  <= >= in math               use \leq \geq
  ... for ellipsis            use \ldots
  x for multiply              use \times
  plain n outside dollar      use $
  double backslash mid-text   only valid inside tabular/align