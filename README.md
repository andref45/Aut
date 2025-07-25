# COMPILADOR - ANÁLISIS SINTÁCTICO
**Examen de Compiladores**

---

## 1. GRAMÁTICA

### Gramática Original:
```
1)  Instr  → Sent ;
2)  Sent   → entero id
3)         → id = E
4)         → escribir ( E )
5)         → si ( E OpRel E ) { Sent ; }
6)         → mientras ( E OpRel E ) { Sent ; }
7)  OpRel  → >
8)         → ==
9)  E      → E + T
10)        → T
11) T      → T * F
12)        → F
13) F      → ( E )
14)        → id
15)        → num
```

### Gramática Aumentada:
```
0)  S'     → Instr $
1)  Instr  → Sent ;
2)  Sent   → entero id
3)         → id = E
4)         → escribir ( E )
5)         → si ( E OpRel E ) { Sent ; }
6)         → mientras ( E OpRel E ) { Sent ; }
7)  OpRel  → >
8)         → ==
9)  E      → E + T
10)        → T
11) T      → T * F
12)        → F
13) F      → ( E )
14)        → id
15)        → num
```

---

## 2. CONJUNTOS FIRST

### Definición:
FIRST(α) = conjunto de terminales que pueden aparecer al inicio de las cadenas derivadas de α.

### Cálculo de FIRST:

**FIRST(S')** = { entero, id, escribir, si, mientras }

**FIRST(Instr)** = { entero, id, escribir, si, mientras }
- Porque Instr → Sent ; y FIRST(Sent) = { entero, id, escribir, si, mientras }

**FIRST(Sent)** = { entero, id, escribir, si, mientras }
- Sent → entero id ⟹ { entero }
- Sent → id = E ⟹ { id }
- Sent → escribir ( E ) ⟹ { escribir }
- Sent → si ( E OpRel E ) { Sent ; } ⟹ { si }
- Sent → mientras ( E OpRel E ) { Sent ; } ⟹ { mientras }

**FIRST(OpRel)** = { >, == }
- OpRel → > ⟹ { > }
- OpRel → == ⟹ { == }

**FIRST(E)** = { (, id, num }
- E → E + T ⟹ FIRST(E) = { (, id, num }
- E → T ⟹ FIRST(T) = { (, id, num }

**FIRST(T)** = { (, id, num }
- T → T * F ⟹ FIRST(T) = { (, id, num }
- T → F ⟹ FIRST(F) = { (, id, num }

**FIRST(F)** = { (, id, num }
- F → ( E ) ⟹ { ( }
- F → id ⟹ { id }
- F → num ⟹ { num }

---

## 3. CONJUNTOS FOLLOW

### Definición:
FOLLOW(A) = conjunto de terminales que pueden aparecer inmediatamente después del no terminal A en alguna forma sentencial.

### Cálculo de FOLLOW:

**FOLLOW(S')** = { $ }
- Por definición, $ ∈ FOLLOW(S')

**FOLLOW(Instr)** = { $ }
- S' → Instr $ ⟹ $ ∈ FOLLOW(Instr)

**FOLLOW(Sent)** = { ; }
- Instr → Sent ; ⟹ ; ∈ FOLLOW(Sent)
- si ( E OpRel E ) { Sent ; } ⟹ ; ∈ FOLLOW(Sent)
- mientras ( E OpRel E ) { Sent ; } ⟹ ; ∈ FOLLOW(Sent)

**FOLLOW(OpRel)** = { (, id, num }
- si ( E OpRel E ) { Sent ; } ⟹ FIRST(E) ∈ FOLLOW(OpRel)
- mientras ( E OpRel E ) { Sent ; } ⟹ FIRST(E) ∈ FOLLOW(OpRel)
- FIRST(E) = { (, id, num }

**FOLLOW(E)** = { +, ), >, ==, ; }
- E → E + T ⟹ + ∈ FOLLOW(E)
- escribir ( E ) ⟹ ) ∈ FOLLOW(E)
- F → ( E ) ⟹ ) ∈ FOLLOW(E)
- si ( E OpRel E ) ⟹ FIRST(OpRel) ∈ FOLLOW(E) = { >, == }
- mientras ( E OpRel E ) ⟹ FIRST(OpRel) ∈ FOLLOW(E) = { >, == }
- si ( E OpRel E ) { Sent ; } ⟹ ) ∈ FOLLOW(E) (después del segundo E)
- mientras ( E OpRel E ) { Sent ; } ⟹ ) ∈ FOLLOW(E) (después del segundo E)

**FOLLOW(T)** = { *, +, ), >, ==, ; }
- E → E + T ⟹ FOLLOW(E) ∈ FOLLOW(T) = { +, ), >, ==, ; }
- T → T * F ⟹ * ∈ FOLLOW(T)
- E → T ⟹ FOLLOW(E) ∈ FOLLOW(T)

**FOLLOW(F)** = { *, +, ), >, ==, ; }
- T → T * F ⟹ FOLLOW(T) ∈ FOLLOW(F) = { *, +, ), >, ==, ; }
- T → F ⟹ FOLLOW(T) ∈ FOLLOW(F)

---

## 4. CONJUNTOS DE ELEMENTOS

### I₀ = CLOSURE({ [S' → •Instr $] })
```
S' → •Instr $
Instr → •Sent ;
Sent → •entero id
Sent → •id = E
Sent → •escribir ( E )
Sent → •si ( E OpRel E ) { Sent ; }
Sent → •mientras ( E OpRel E ) { Sent ; }
```

### I₁ = GOTO(I₀, Instr)
```
S' → Instr•$
```

### I₂ = GOTO(I₀, Sent)
```
Instr → Sent•;
```

### I₃ = GOTO(I₀, entero)
```
Sent → entero•id
```

### I₄ = GOTO(I₀, id)
```
Sent → id•= E
```

### I₅ = GOTO(I₀, escribir)
```
Sent → escribir•( E )
```

### I₆ = GOTO(I₀, si)
```
Sent → si•( E OpRel E ) { Sent ; }
```

### I₇ = GOTO(I₀, mientras)
```
Sent → mientras•( E OpRel E ) { Sent ; }
```

### I₈ = GOTO(I₁, $)
```
S' → Instr $•
```

### I₉ = GOTO(I₂, ;)
```
Instr → Sent ;•
```

### I₁₀ = GOTO(I₃, id)
```
Sent → entero id•
```

### I₁₁ = GOTO(I₄, =)
```
Sent → id =•E
E → •E + T
E → •T
T → •T * F
T → •F
F → •( E )
F → •id
F → •num
```

### I₁₂ = GOTO(I₅, ()
```
Sent → escribir (•E )
E → •E + T
E → •T
T → •T * F
T → •F
F → •( E )
F → •id
F → •num
```

### I₁₃ = GOTO(I₆, ()
```
Sent → si (•E OpRel E ) { Sent ; }
E → •E + T
E → •T
T → •T * F
T → •F
F → •( E )
F → •id
F → •num
```

### I₁₄ = GOTO(I₇, ()
```
Sent → mientras (•E OpRel E ) { Sent ; }
E → •E + T
E → •T
T → •T * F
T → •F
F → •( E )
F → •id
F → •num
```

### I₁₅ = GOTO(I₁₁, E)
```
Sent → id = E•
E → E•+ T
```

### I₁₆ = GOTO(I₁₁, T)
```
E → T•
T → T•* F
```

### I₁₇ = GOTO(I₁₁, F)
```
T → F•
```

### I₁₈ = GOTO(I₁₁, ()
```
F → (•E )
E → •E + T
E → •T
T → •T * F
T → •F
F → •( E )
F → •id
F → •num
```

### I₁₉ = GOTO(I₁₁, id)
```
F → id•
```

### I₂₀ = GOTO(I₁₁, num)
```
F → num•
```

### I₂₁ = GOTO(I₁₂, E)
```
Sent → escribir ( E•)
E → E•+ T
```

### I₂₂ = GOTO(I₁₃, E)
```
Sent → si ( E•OpRel E ) { Sent ; }
E → E•+ T
```

### I₂₃ = GOTO(I₁₄, E)
```
Sent → mientras ( E•OpRel E ) { Sent ; }
E → E•+ T
```

### I₂₄ = GOTO(I₁₅, +)
```
E → E +•T
T → •T * F
T → •F
F → •( E )
F → •id
F → •num
```

### I₂₅ = GOTO(I₁₆, *)
```
T → T *•F
F → •( E )
F → •id
F → •num
```

### I₂₆ = GOTO(I₁₈, E)
```
F → ( E•)
E → E•+ T
```

### I₂₇ = GOTO(I₂₁, ))
```
Sent → escribir ( E )•
```

### I₂₈ = GOTO(I₂₂, OpRel)
```
Sent → si ( E OpRel•E ) { Sent ; }
E → •E + T
E → •T
T → •T * F
T → •F
F → •( E )
F → •id
F → •num
```

### I₂₉ = GOTO(I₂₃, OpRel)
```
Sent → mientras ( E OpRel•E ) { Sent ; }
E → •E + T
E → •T
T → •T * F
T → •F
F → •( E )
F → •id
F → •num
```

### I₃₀ = GOTO(I₂₄, T)
```
E → E + T•
T → T•* F
```

### I₃₁ = GOTO(I₂₅, F)
```
T → T * F•
```

### I₃₂ = GOTO(I₂₆, ))
```
F → ( E )•
```

### I₃₃ = GOTO(I₂₂, >)
```
Sent → si ( E >•E ) { Sent ; }
E → •E + T
E → •T
T → •T * F
T → •F
F → •( E )
F → •id
F → •num
```

### I₃₄ = GOTO(I₂₂, ==)
```
Sent → si ( E ==•E ) { Sent ; }
E → •E + T
E → •T
T → •T * F
T → •F
F → •( E )
F → •id
F → •num
```

### I₃₅ = GOTO(I₂₃, >)
```
Sent → mientras ( E >•E ) { Sent ; }
E → •E + T
E → •T
T → •T * F
T → •F
F → •( E )
F → •id
F → •num
```

### I₃₆ = GOTO(I₂₃, ==)
```
Sent → mientras ( E ==•E ) { Sent ; }
E → •E + T
E → •T
T → •T * F
T → •F
F → •( E )
F → •id
F → •num
```

### I₃₇ = GOTO(I₂₈, E)
```
Sent → si ( E OpRel E•) { Sent ; }
E → E•+ T
```

### I₃₈ = GOTO(I₂₉, E)
```
Sent → mientras ( E OpRel E•) { Sent ; }
E → E•+ T
```

### I₃₉ = GOTO(I₃₃, E)
```
Sent → si ( E > E•) { Sent ; }
E → E•+ T
```

### I₄₀ = GOTO(I₃₄, E)
```
Sent → si ( E == E•) { Sent ; }
E → E•+ T
```

### I₄₁ = GOTO(I₃₅, E)
```
Sent → mientras ( E > E•) { Sent ; }
E → E•+ T
```

### I₄₂ = GOTO(I₃₆, E)
```
Sent → mientras ( E == E•) { Sent ; }
E → E•+ T
```

### I₄₃ = GOTO(I₃₇, ))
```
Sent → si ( E OpRel E )•{ Sent ; }
```

### I₄₄ = GOTO(I₃₈, ))
```
Sent → mientras ( E OpRel E )•{ Sent ; }
```

### I₄₅ = GOTO(I₃₉, ))
```
Sent → si ( E > E )•{ Sent ; }
```

### I₄₆ = GOTO(I₄₀, ))
```
Sent → si ( E == E )•{ Sent ; }
```

### I₄₇ = GOTO(I₄₁, ))
```
Sent → mientras ( E > E )•{ Sent ; }
```

### I₄₈ = GOTO(I₄₂, ))
```
Sent → mientras ( E == E )•{ Sent ; }
```

### I₄₉ = GOTO(I₄₃, {)
```
Sent → si ( E OpRel E ) {•Sent ; }
Sent → •entero id
Sent → •id = E
Sent → •escribir ( E )
Sent → •si ( E OpRel E ) { Sent ; }
Sent → •mientras ( E OpRel E ) { Sent ; }
```

### I₅₀ = GOTO(I₄₄, {)
```
Sent → mientras ( E OpRel E ) {•Sent ; }
Sent → •entero id
Sent → •id = E
Sent → •escribir ( E )
Sent → •si ( E OpRel E ) { Sent ; }
Sent → •mientras ( E OpRel E ) { Sent ; }
```

### I₅₁ = GOTO(I₄₅, {)
```
Sent → si ( E > E ) {•Sent ; }
Sent → •entero id
Sent → •id = E
Sent → •escribir ( E )
Sent → •si ( E OpRel E ) { Sent ; }
Sent → •mientras ( E OpRel E ) { Sent ; }
```

### I₅₂ = GOTO(I₄₆, {)
```
Sent → si ( E == E ) {•Sent ; }
Sent → •entero id
Sent → •id = E
Sent → •escribir ( E )
Sent → •si ( E OpRel E ) { Sent ; }
Sent → •mientras ( E OpRel E ) { Sent ; }
```

### I₅₃ = GOTO(I₄₇, {)
```
Sent → mientras ( E > E ) {•Sent ; }
Sent → •entero id
Sent → •id = E
Sent → •escribir ( E )
Sent → •si ( E OpRel E ) { Sent ; }
Sent → •mientras ( E OpRel E ) { Sent ; }
```

### I₅₄ = GOTO(I₄₈, {)
```
Sent → mientras ( E == E ) {•Sent ; }
Sent → •entero id
Sent → •id = E
Sent → •escribir ( E )
Sent → •si ( E OpRel E ) { Sent ; }
Sent → •mientras ( E OpRel E ) { Sent ; }
```

### I₅₅ = GOTO(I₄₉, Sent)
```
Sent → si ( E OpRel E ) { Sent•; }
```

### I₅₆ = GOTO(I₅₀, Sent)
```
Sent → mientras ( E OpRel E ) { Sent•; }
```

### I₅₇ = GOTO(I₅₁, Sent)
```
Sent → si ( E > E ) { Sent•; }
```

### I₅₈ = GOTO(I₅₂, Sent)
```
Sent → si ( E == E ) { Sent•; }
```

### I₅₉ = GOTO(I₅₃, Sent)
```
Sent → mientras ( E > E ) { Sent•; }
```

### I₆₀ = GOTO(I₅₄, Sent)
```
Sent → mientras ( E == E ) { Sent•; }
```

### I₆₁ = GOTO(I₅₅, ;)
```
Sent → si ( E OpRel E ) { Sent ;•}
```

### I₆₂ = GOTO(I₅₆, ;)
```
Sent → mientras ( E OpRel E ) { Sent ;•}
```

### I₆₃ = GOTO(I₅₇, ;)
```
Sent → si ( E > E ) { Sent ;•}
```

### I₆₄ = GOTO(I₅₈, ;)
```
Sent → si ( E == E ) { Sent ;•}
```

### I₆₅ = GOTO(I₅₉, ;)
```
Sent → mientras ( E > E ) { Sent ;•}
```

### I₆₆ = GOTO(I₆₀, ;)
```
Sent → mientras ( E == E ) { Sent ;•}
```

### I₆₇ = GOTO(I₆₁, })
```
Sent → si ( E OpRel E ) { Sent ; }•
```

### I₆₈ = GOTO(I₆₂, })
```
Sent → mientras ( E OpRel E ) { Sent ; }•
```

### I₆₉ = GOTO(I₆₃, })
```
Sent → si ( E > E ) { Sent ; }•
```

### I₇₀ = GOTO(I₆₄, })
```
Sent → si ( E == E ) { Sent ; }•
```

### I₇₁ = GOTO(I₆₅, })
```
Sent → mientras ( E > E ) { Sent ; }•
```

### I₇₂ = GOTO(I₆₆, })
```
Sent → mientras ( E == E ) { Sent ; }•
```

---

## 5. TABLA DE ANÁLISIS SINTÁCTICO

### Tabla de Acciones (Terminales)

| Estado | entero | id  | escribir | si  | mientras | =   | +   | *   | (   | )   | >   | ==  | ;   | $   |
|--------|--------|-----|----------|-----|----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 0      | d2     | d3  | d4       | d5  | d6       | -   | -   | -   | -   | -   | -   | -   | -   | -   |
| 1      | -      | -   | -        | -   | -        | -   | -   | -   | -   | -   | -   | -   | -   | acc |
| 2      | -      | d7  | -        | -   | -        | -   | -   | -   | -   | -   | -   | -   | -   | -   |
| 3      | -      | -   | -        | -   | -        | d8  | -   | -   | -   | -   | -   | -   | -   | -   |
| 4      | -      | -   | -        | -   | -        | -   | -   | -   | d9  | -   | -   | -   | -   | -   |
| 5      | -      | -   | -        | -   | -        | -   | -   | -   | d10 | -   | -   | -   | -   | -   |
| 6      | -      | -   | -        | -   | -        | -   | -   | -   | d11 | -   | -   | -   | -   | -   |
| 7      | -      | -   | -        | -   | -        | -   | -   | -   | -   | -   | -   | -   | r2  | -   |
| 8      | -      | d13 | -        | -   | -        | -   | -   | -   | d12 | -   | -   | -   | -   | -   |
| 9      | -      | d13 | -        | -   | -        | -   | -   | -   | d12 | -   | -   | -   | -   | -   |
| 10     | -      | d13 | -        | -   | -        | -   | -   | -   | d12 | -   | -   | -   | -   | -   |
| 11     | -      | d13 | -        | -   | -        | -   | -   | -   | d12 | -   | -   | -   | -   | -   |
| 12     | -      | d13 | -        | -   | -        | -   | -   | -   | d12 | -   | -   | -   | -   | -   |
| 13     | -      | -   | -        | -   | -        | -   | r14 | r14 | -   | r14 | r14 | r14 | r14 | -   |
| 14     | -      | -   | -        | -   | -        | -   | r15 | r15 | -   | r15 | r15 | r15 | r15 | -   |
| 15     | -      | -   | -        | -   | -        | -   | d16 | -   | -   | r3  | r3  | r3  | r3  | -   |
| 16     | -      | d13 | -        | -   | -        | -   | -   | -   | d12 | -   | -   | -   | -   | -   |
| 17     | -      | d13 | -        | -   | -        | -   | -   | -   | d12 | -   | -   | -   | -   | -   |
| 18     | -      | d13 | -        | -   | -        | -   | -   | -   | d12 | -   | -   | -   | -   | -   |
| 19     | -      | d13 | -        | -   | -        | -   | -   | -   | d12 | -   | -   | -   | -   | -   |
| 20     | -      | -   | -        | -   | -        | -   | r10 | r10 | -   | r10 | r10 | r10 | r10 | -   |
| 21     | -      | -   | -        | -   | -        | -   | r12 | d22 | -   | r12 | r12 | r12 | r12 | -   |
| 22     | -      | d13 | -        | -   | -        | -   | -   | -   | d12 | -   | -   | -   | -   | -   |
| 23     | -      | -   | -        | -   | -        | -   | d16 | -   | -   | d24 | -   | -   | -   | -   |
| 24     | -      | -   | -        | -   | -        | -   | r4  | r4  | -   | r4  | r4  | r4  | r4  | -   |
| 25     | -      | -   | -        | -   | -        | -   | d16 | -   | -   | -   | d26 | d27 | -   | -   |
| 26     | -      | d13 | -        | -   | -        | -   | -   | -   | d12 | -   | -   | -   | -   | -   |
| 27     | -      | d13 | -        | -   | -        | -   | -   | -   | d12 | -   | -   | -   | -   | -   |
| 28     | -      | -   | -        | -   | -        | -   | d16 | -   | -   | -   | d26 | d27 | -   | -   |
| 29     | -      | -   | -        | -   | -        | -   | d16 | -   | -   | d30 | -   | -   | -   | -   |
| 30     | -      | -   | -        | -   | -        | -   | -   | -   | -   | -   | -   | -   | -   | -   |
| 31     | d2     | d3  | d4       | d5  | d6       | -   | -   | -   | -   | -   | -   | -   | -   | -   |
| 32     | -      | -   | -        | -   | -        | -   | -   | -   | -   | -   | -   | -   | d33 | -   |
| 33     | -      | -   | -        | -   | -        | -   | -   | -   | -   | -   | -   | -   | -   | -   |
| 34     | -      | -   | -        | -   | -        | -   | r5  | r5  | -   | r5  | r5  | r5  | r5  | -   |
| 35     | -      | -   | -        | -   | -        | -   | d16 | -   | -   | d36 | -   | -   | -   | -   |
| 36     | -      | -   | -        | -   | -        | -   | -   | -   | -   | -   | -   | -   | -   | -   |
| 37     | d2     | d3  | d4       | d5  | d6       | -   | -   | -   | -   | -   | -   | -   | -   | -   |
| 38     | -      | -   | -        | -   | -        | -   | -   | -   | -   | -   | -   | -   | d39 | -   |
| 39     | -      | -   | -        | -   | -        | -   | -   | -   | -   | -   | -   | -   | -   | -   |
| 40     | -      | -   | -        | -   | -        | -   | r6  | r6  | -   | r6  | r6  | r6  | r6  | -   |
| 41     | -      | -   | -        | -   | -        | -   | r9  | d22 | -   | r9  | r9  | r9  | r9  | -   |
| 42     | -      | -   | -        | -   | -        | -   | r11 | r11 | -   | r11 | r11 | r11 | r11 | -   |
| 43     | -      | -   | -        | -   | -        | -   | r13 | r13 | -   | r13 | r13 | r13 | r13 | -   |
| 44     | -      | -   | -        | -   | -        | -   | -   | -   | -   | -   | -   | -   | d45 | -   |
| 45     | -      | -   | -        | -   | -        | -   | r1  | r1  | -   | r1  | r1  | r1  | r1  | r1  |

### Tabla GOTO (No Terminales)

| Estado | Instr | Sent | E  | OpRel | T  | F  |
|--------|-------|------|----|----- -|----|----|
| 0      | 1     | 44   | -  | -     | -  | -  |
| 8      | -     | -    | 15 | -     | 20 | 21 |
| 9      | -     | -    | 23 | -     | 20 | 21 |
| 10     | -     | -    | 25 | -     | 20 | 21 |
| 11     | -     | -    | 28 | -     | 20 | 21 |
| 12     | -     | -    | 23 | -     | 20 | 21 |
| 16     | -     | -    | -  | -     | 41 | 21 |
| 17     | -     | -    | -  | -     | 41 | 21 |
| 18     | -     | -    | -  | -     | 41 | 21 |
| 19     | -     | -    | -  | -     | 41 | 21 |
| 22     | -     | -    | -  | -     | -  | 42 |
| 26     | -     | -    | 29 | -     | 20 | 21 |
| 27     | -     | -    | 29 | -     | 20 | 21 |
| 31     | -     | 32   | -  | -     | -  | -  |
| 37     | -     | 38   | -  | -     | -  | -  |

### Leyenda:
- **d##**: desplazar y meter en la pila el estado ##
- **r##**: reducir por la producción con número ##
- **acc**: aceptar
- **-**: error

---

## 6. CONJUNTO DE ESTADOS

| Conjunto | Elemento |
|----------|----------|
| I0 | S' → •Instr $ |
| I0 | Instr → •Sent ; |
| I0 | Sent → •entero id |
| I0 | Sent → •id = E |
| I0 | Sent → •escribir ( E ) |
| I0 | Sent → •si ( E OpRel E ) { Sent ; } |
| I0 | Sent → •mientras ( E OpRel E ) { Sent ; } |
| I1 | S' → Instr•$ |
| I2 | Instr → Sent•; |
| I3 | Sent → entero•id |
| I4 | Sent → id•= E |
| I5 | Sent → escribir•( E ) |
| I6 | Sent → si•( E OpRel E ) { Sent ; } |
| I7 | Sent → mientras•( E OpRel E ) { Sent ; } |
| I8 | S' → Instr $• |
| I9 | Instr → Sent ;• |
| I10 | Sent → entero id• |
| I11 | Sent → id =•E |
| I11 | E → •E + T |
| I11 | E → •T |
| I11 | T → •T * F |
| I11 | T → •F |
| I11 | F → •( E ) |
| I11 | F → •id |
| I11 | F → •num |
| I12 | Sent → escribir (•E ) |
| I12 | E → •E + T |
| I12 | E → •T |
| I12 | T → •T * F |
| I12 | T → •F |
| I12 | F → •( E ) |
| I12 | F → •id |
| I12 | F → •num |
| I13 | Sent → si (•E OpRel E ) { Sent ; } |
| I13 | E → •E + T |
| I13 | E → •T |
| I13 | T → •T * F |
| I13 | T → •F |
| I13 | F → •( E ) |
| I13 | F → •id |
| I13 | F → •num |
| I14 | Sent → mientras (•E OpRel E ) { Sent ; } |
| I14 | E → •E + T |
| I14 | E → •T |
| I14 | T → •T * F |
| I14 | T → •F |
| I14 | F → •( E ) |
| I14 | F → •id |
| I14 | F → •num |
| I15 | Sent → id = E• |
| I15 | E → E•+ T |
| I16 | E → T• |
| I16 | T → T•* F |
| I17 | T → F• |
| I18 | F → (•E ) |
| I18 | E → •E + T |
| I18 | E → •T |
| I18 | T → •T * F |
| I18 | T → •F |
| I18 | F → •( E ) |
| I18 | F → •id |
| I18 | F → •num |
| I19 | F → id• |
| I20 | F → num• |
| I21 | Sent → escribir ( E•) |
| I21 | E → E•+ T |
| I22 | Sent → si ( E•OpRel E ) { Sent ; } |
| I22 | E → E•+ T |
| I23 | Sent → mientras ( E•OpRel E ) { Sent ; } |
| I23 | E → E•+ T |
| I24 | E → E +•T |
| I24 | T → •T * F |
| I24 | T → •F |
| I24 | F → •( E ) |
| I24 | F → •id |
| I24 | F → •num |
| I25 | T → T *•F |
| I25 | F → •( E ) |
| I25 | F → •id |
| I25 | F → •num |
| I26 | F → ( E•) |
| I26 | E → E•+ T |
| I27 | Sent → escribir ( E )• |
| I28 | Sent → si ( E OpRel•E ) { Sent ; } |
| I28 | E → •E + T |
| I28 | E → •T |
| I28 | T → •T * F |
| I28 | T → •F |
| I28 | F → •( E ) |
| I28 | F → •id |
| I28 | F → •num |
| I29 | Sent → mientras ( E OpRel•E ) { Sent ; } |
| I29 | E → •E + T |
| I29 | E → •T |
| I29 | T → •T * F |
| I29 | T → •F |
| I29 | F → •( E ) |
| I29 | F → •id |
| I29 | F → •num |
| I30 | E → E + T• |
| I30 | T → T•* F |
| I31 | T → T * F• |
| I32 | F → ( E )• |
| I33 | Sent → si ( E >•E ) { Sent ; } |
| I33 | E → •E + T |
| I33 | E → •T |
| I33 | T → •T * F |
| I33 | T → •F |
| I33 | F → •( E ) |
| I33 | F → •id |
| I33 | F → •num |
| I34 | Sent → si ( E ==•E ) { Sent ; } |
| I34 | E → •E + T |
| I34 | E → •T |
| I34 | T → •T * F |
| I34 | T → •F |
| I34 | F → •( E ) |
| I34 | F → •id |
| I34 | F → •num |
| I35 | Sent → mientras ( E >•E ) { Sent ; } |
| I35 | E → •E + T |
| I35 | E → •T |
| I35 | T → •T * F |
| I35 | T → •F |
| I35 | F → •( E ) |
| I35 | F → •id |
| I35 | F → •num |
| I36 | Sent → mientras ( E ==•E ) { Sent ; } |
| I36 | E → •E + T |
| I36 | E → •T |
| I36 | T → •T * F |
| I36 | T → •F |
| I36 | F → •( E ) |
| I36 | F → •id |
| I36 | F → •num |
| I37 | Sent → si ( E OpRel E•) { Sent ; } |
| I37 | E → E•+ T |
| I38 | Sent → mientras ( E OpRel E•) { Sent ; } |
| I38 | E → E•+ T |
| I39 | Sent → si ( E > E•) { Sent ; } |
| I39 | E → E•+ T |
| I40 | Sent → si ( E == E•) { Sent ; } |
| I40 | E → E•+ T |
| I41 | Sent → mientras ( E > E•) { Sent ; } |
| I41 | E → E•+ T |
| I42 | Sent → mientras ( E == E•) { Sent ; } |
| I42 | E → E•+ T |
| I43 | Sent → si ( E OpRel E )•{ Sent ; } |
| I44 | Sent → mientras ( E OpRel E )•{ Sent ; } |
| I45 | Sent → si ( E > E )•{ Sent ; } |
| I46 | Sent → si ( E == E )•{ Sent ; } |
| I47 | Sent → mientras ( E > E )•{ Sent ; } |
| I48 | Sent → mientras ( E == E )•{ Sent ; } |
| I49 | Sent → si ( E OpRel E ) {•Sent ; } |
| I49 | Sent → •entero id |
| I49 | Sent → •id = E |
| I49 | Sent → •escribir ( E ) |
| I49 | Sent → •si ( E OpRel E ) { Sent ; } |
| I49 | Sent → •mientras ( E OpRel E ) { Sent ; } |
| I50 | Sent → mientras ( E OpRel E ) {•Sent ; } |
| I50 | Sent → •entero id |
| I50 | Sent → •id = E |
| I50 | Sent → •escribir ( E ) |
| I50 | Sent → •si ( E OpRel E ) { Sent ; } |
| I50 | Sent → •mientras ( E OpRel E ) { Sent ; } |
| I51 | Sent → si ( E > E ) {•Sent ; } |
| I51 | Sent → •entero id |
| I51 | Sent → •id = E |
| I51 | Sent → •escribir ( E ) |
| I51 | Sent → •si ( E OpRel E ) { Sent ; } |
| I51 | Sent → •mientras ( E OpRel E ) { Sent ; } |
| I52 | Sent → si ( E == E ) {•Sent ; } |
| I52 | Sent → •entero id |
| I52 | Sent → •id = E |
| I52 | Sent → •escribir ( E ) |
| I52 | Sent → •si ( E OpRel E ) { Sent ; } |
| I52 | Sent → •mientras ( E OpRel E ) { Sent ; } |
| I53 | Sent → mientras ( E > E ) {•Sent ; } |
| I53 | Sent → •entero id |
| I53 | Sent → •id = E |
| I53 | Sent → •escribir ( E ) |
| I53 | Sent → •si ( E OpRel E ) { Sent ; } |
| I53 | Sent → •mientras ( E OpRel E ) { Sent ; } |
| I54 | Sent → mientras ( E == E ) {•Sent ; } |
| I54 | Sent → •entero id |
| I54 | Sent → •id = E |
| I54 | Sent → •escribir ( E ) |
| I54 | Sent → •si ( E OpRel E ) { Sent ; } |
| I54 | Sent → •mientras ( E OpRel E ) { Sent ; } |
| I55 | Sent → si ( E OpRel E ) { Sent•; } |
| I56 | Sent → mientras ( E OpRel E ) { Sent•; } |
| I57 | Sent → si ( E > E ) { Sent•; } |
| I58 | Sent → si ( E == E ) { Sent•; } |
| I59 | Sent → mientras ( E > E ) { Sent•; } |
| I60 | Sent → mientras ( E == E ) { Sent•; } |
| I61 | Sent → si ( E OpRel E ) { Sent ;•} |
| I62 | Sent → mientras ( E OpRel E ) { Sent ;•} |
| I63 | Sent → si ( E > E ) { Sent ;•} |
| I64 | Sent → si ( E == E ) { Sent ;•} |
| I65 | Sent → mientras ( E > E ) { Sent ;•} |
| I66 | Sent → mientras ( E == E ) { Sent ;•} |
| I67 | Sent → si ( E OpRel E ) { Sent ; }• |
| I68 | Sent → mientras ( E OpRel E ) { Sent ; }• |
| I69 | Sent → si ( E > E ) { Sent ; }• |
| I70 | Sent → si ( E == E ) { Sent ; }• |
| I71 | Sent → mientras ( E > E ) { Sent ; }• |
| I72 | Sent → mientras ( E == E ) { Sent ; }• |

---

## ALGORITMO DE ANÁLISIS SINTÁCTICO LR(1)

### Pseudocódigo del Analizador:

```
1. Inicializar pila con estado 0
2. Apuntar ae al primer símbolo de entrada w$
3. Repetir para siempre:
   a. Sea s el estado en la cima de la pila
   b. Sea a el símbolo apuntado por ae
   c. Si acción[s,a] = desplazar s' entonces:
      - Meter a y después s' en la cima de la pila
      - Avanzar ae al siguiente símbolo de entrada
   d. Si acción[s,a] = reducir A → β entonces:
      - Sacar 2*|β| símbolos de la pila
      - Sea s' el estado que ahora está en la cima de la pila
      - Meter A y después ir_a[s',A] en la cima de la pila
   e. Si acción[s,a] = aceptar entonces:
      - return (análisis exitoso)
   f. Si no:
      - error()
```

### Códigos de Acciones:
- **d##**: desplazar y meter en la pila el estado ##
- **r##**: reducir por la producción con número ##
- **acc**: aceptar
- **-**: error

---

**Nombre:** ___________________  
**Fecha:** ____________________  
**Curso:** ____________________

---

## EJEMPLOS DE CADENAS VÁLIDAS

### Ejemplo 1: Declaración de variable
```
entero x ;
```

### Ejemplo 2: Asignación
```
x = 5 + 3 * 2 ;
```

### Ejemplo 3: Instrucción de escritura
```
escribir ( x + 1 ) ;
```

### Ejemplo 4: Condicional simple
```
si ( x > 0 ) { escribir ( x ) ; }
```

### Ejemplo 5: Bucle while
```
mientras ( x == 5 ) { x = x + 1 ; }
```

---

## NOTAS IMPORTANTES

1. **Precedencia de operadores**: El operador * tiene mayor precedencia que +
2. **Asociatividad**: Ambos operadores son asociativos por la izquierda
3. **Gramática LR(1)**: Esta gramática es LR(1) por lo que no presenta conflictos
4. **Estados de aceptación**: Solo el estado 1 tiene la acción de aceptar
5. **Estados de error**: Las celdas vacías (-) representan errores sintácticos

---

**FIN DEL DOCUMENTO**
