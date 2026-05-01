# Polygon Statements TeX Manual

Source: https://polygon.codeforces.com/docs/statements-tex-manual  
**This is the AUTHORITATIVE reference. The agent MUST read this before writing any statement file.**

---

## Complete list of supported HTML commands

Only these commands render correctly in HTML. Anything outside this list breaks silently.  
Inside math mode `$ ... $`: any MathJax/LaTeX math symbol is supported.

### Text formatting

| Command | Result |
|---|---|
| `\textbf{text}` or `\bf{text}` | **bold** |
| `\textit{text}` or `\it{text}` | *italic* |
| `\t{text}` or `\tt{text}` or `\texttt{text}` | `monospace` — use for literal tokens like `\t{YES}` `\t{NO}` `\t{-1}` |
| `\verb\|text\|` | monospace, allows special characters `"'!@#$^&*` |
| `\emph{text}` or `\underline{text}` | underlined |
| `\sout{text}` | ~~strikethrough~~ |
| `\textsc{text}` | SMALL CAPS |

### Text size

| Command | Size |
|---|---|
| `\tiny{text}` | 70% |
| `\scriptsize{text}` | 75% |
| `\small{text}` | 85% |
| `\normalsize{text}` | 100% (default) |
| `\large{text}` | 115% |
| `\Large{text}` | 130% |
| `\LARGE{text}` | 145% |
| `\huge{text}` | 175% |
| `\Huge{text}` | 200% |

### Lists

Unordered:
```
\begin{itemize}
  \item First item;
  \item Second item.
\end{itemize}
```

Ordered:
```
\begin{enumerate}
  \item First item;
  \item Second item.
\end{enumerate}
```

### Code blocks

```
\begin{lstlisting}
#include <iostream>
int main() {
    int a, b;
    std::cin >> a >> b;
    std::cout << a + b << std::endl;
}
\end{lstlisting}
```

Auto-detects language and applies syntax highlighting.

### Centered content

```
\begin{center}
  This content is centered.
  $abacaba$
\end{center}
```

### Images

Upload the image via **Statement Resource Files** on the Statements page first.

```
\includegraphics{filename.png}                   % unscaled
\includegraphics[scale=1.5]{filename.png}         % scaled
\includegraphics[width=4cm]{filename.png}         % width in cm
```

Recommended (centered with caption):
```
\begin{center}
  \includegraphics[scale=1.0]{filename.png} \\
  \small{Figure caption.}
\end{center}
```

For width in cm, override pixels-per-cm (default 37.8):
```
\begin{center}
  \def \htmlPixelsInCm {45}
  \includegraphics[width=4cm]{filename.png}
\end{center}
```

### Tables

Simple (no borders):
```
\begin{tabular}{ll}
  First & Second \\
  Third & Fourth
\end{tabular}
```

With borders:
```
\begin{tabular}{|l|c|r|}
\hline
  Left & Center & Right \\ \hline
  Text & Text   & Text  \\ \hline
\end{tabular}
```

Scoring table (common pattern):
```
\begin{center}
  \begin{tabular}{|c|c|c|c|}
  \hline
    \textbf{Group} & \textbf{Constraints} & \textbf{Points} & \textbf{Req.} \\ \hline
    $1$ & $n \le 10$  & $12$ & ---         \\ \hline
    $2$ & $n \le 500$ & $19$ & ---         \\ \hline
    $3$ & ---         & $41$ & ---         \\ \hline
    $4$ & ---         & $28$ & $1$, $2$, $3$ \\ \hline
  \end{tabular}
\end{center}
```

Column/row span:
```
\multicolumn{2}{|c|}{\textbf{Header}}   % spans 2 columns, centered, with border
\multirow{2}{*}{text}                    % spans 2 rows
\cline{2-3}                              % partial horizontal line cols 2–3
```

### Hyperlinks

```
\url{https://codeforces.com/}
\href{https://codeforces.com/}{Codeforces}
```

### Epigraph

```
\epigraph{\textit{Some inspirational citation...}}{--- Author, \textit{Source}}
Legend starts here...
```

---

## Math mode

All problems created after June 2021 use MathJax — any LaTeX math symbol works.

Inline (part of text):
```
$x$
$a_i^2 + b_i^2 \le a_{i+1}^2$
```

Display/centered (own line):
```
$$x$$
$$a_i^2 + b_i^2 \le a_{i+1}^2$$
```

Common math symbols:
```
\le  \ge  \ne            less/greater/not-equal (also \leq \geq \neq)
\times                   multiplication: $n \times m$
\ldots                   ellipsis in sequence: $a_1, a_2, \ldots, a_n$
\cdots                   ellipsis in sum: $a_1 + a_2 + \cdots + a_n$
\sum_{i=1}^{n}           summation
\frac{a}{b}              fraction
\sqrt{x}                 square root
\lfloor x \rfloor        floor
\lceil x \rceil          ceiling
\log  \ln                logarithm
\binom{n}{k}             binomial
\text{word}              text inside math: $\text{target}$
a_i   a_{ij}             subscript
n^2   2^{10}             superscript
\longrightarrow          long right arrow: $3 \longrightarrow 12$
\blacksquare             black square marker
```

---

## Quotation marks and dashes (English statements)

```
``these double quotes''     renders as "these double quotes"
`a'                         renders as 'a' (single quote)
"---                        renders as em-dash (—)
```

---

## Paragraphs

A **blank line** (two newlines) creates a new paragraph.  
A single newline does NOT create a paragraph break.

```
First paragraph. Still first paragraph.

Second paragraph.    <- blank line above starts new paragraph
```

---

## FORBIDDEN — do NOT use in any statement file

These commands are NOT supported in HTML and will break rendering:

```
\usepackage{...}       Polygon manages packages — remove entirely
\begin{document}       Polygon wraps this — remove entirely
\documentclass{...}   Polygon sets this — remove entirely
\newcommand{...}       use defs.toml for custom macros instead
\section{...}          not supported — use \textbf{} or \large{} for headings
\begin{verbatim}       not supported — use \begin{lstlisting} or \t{} or \verb
\begin{equation}       not supported — use $$ ... $$ for display math
\begin{align}          not supported in HTML — use $$ ... $$ with \\
```

---

## Strict rules for the agent

1. **Read this file completely before writing any statement file.**
2. Use ONLY commands from the "Supported HTML commands" list above.
3. All variables and math expressions in math mode: `$n$` `$a_i$` `$k$` — never plain text.
4. Math symbols: `\le` `\ge` `\ne` `\times` `\ldots` `\cdots` — never `<=` `>=` `!=` `x` `...`
5. Literal tokens: `\t{YES}` `\t{NO}` `\t{-1}` — never plain `YES` or `-1` in output description.
6. Em-dash in English: `"---` (quote + three dashes). Example: `$n$ "--- the number of elements.`
7. New paragraph = blank line. Single newline is NOT a paragraph break.
8. Images: upload via Statement Resource Files first, then use `\includegraphics`.
9. NEVER use `\usepackage` `\begin{document}` `\documentclass` `\newcommand` `\section` `\begin{verbatim}`.
10. For code listings: use `\begin{lstlisting} ... \end{lstlisting}`.
11. For headings inside statements: use `\textbf{Heading}` or `\large{Heading}`.
