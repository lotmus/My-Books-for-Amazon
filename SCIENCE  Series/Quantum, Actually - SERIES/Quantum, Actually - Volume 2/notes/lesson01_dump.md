**Mathematical foundations for quantum states, operators, spinors, and fields**

Course edition 1.0

# How to use this lesson

Quantum electrodynamics is written in the language of complex vector spaces and linear operators. This lesson develops that language from first principles. The emphasis is not only on calculation, but on recognizing the structures that return later as quantum states, observables, spinors, polarization vectors, and field modes.

Work through the examples with pencil and paper. Attempt the exercises before reading the solutions. A learner comfortable with algebra can complete the lesson in six to ten focused hours; mastery comes from repeating the calculations until the notation feels ordinary.

## Learning objectives

- Compute with complex numbers in Cartesian, polar, and exponential form.

- Use complex conjugation and modulus to construct real, nonnegative quantities.

- Interpret vectors abstractly and distinguish vectors from their coordinate columns.

- Use inner products, norms, orthogonality, and orthonormal bases.

- Represent linear maps by matrices and understand how representations change with basis.

- Find eigenvalues and eigenvectors and recognize Hermitian and unitary operators.

- Read elementary bra-ket notation and connect it to ordinary matrix algebra.

- Apply the Pauli matrices as the first concrete bridge to spin and QED.

## Notation and conventions

  ------------------------------------------------------------------------
  **Symbol**                          **Meaning**
  ----------------------------------- ------------------------------------
  i                                   Imaginary unit, i² = -1

  z\*                                 Complex conjugate of z

  ℂⁿ                                  Complex n-dimensional vector space

  v†                                  Conjugate transpose of v

  ⟨u\|v⟩                              Inner product

  I                                   Identity operator

  A⁻¹                                 Inverse of A, when it exists
  ------------------------------------------------------------------------

# 1 Complex numbers

## 1.1 Why quantum theory uses complex numbers

A real number describes magnitude along one line. A complex number carries two real components and, crucially, a phase. Quantum amplitudes interfere: phases can reinforce or cancel even when measurable probabilities remain real. Complex numbers provide the smallest algebraic system that naturally encodes this behavior.

## 1.2 Cartesian form

A complex number has a real part and an imaginary part.

$$z\  = \ a\  + \ ib,\ \ \ \ a,b\  \in \ {\mathbb{R}},\ \ \ \ i²\  = \  - 1$$

Addition is componentwise. Multiplication follows ordinary distributivity together with i² = -1.

$$(a + ib)(c + id)\  = \ (ac - bd)\  + \ i(ad + bc)$$

### Worked example 1

Let z = 3 + 2i and w = 1 - 4i. Then z + w = 4 - 2i. For the product,

$$zw\  = \ (3 + 2i)(1 - 4i)\  = \ 11 - 10i$$

The term (2i)(-4i) equals +8 because i² = -1.

## 1.3 Conjugation and modulus

Complex conjugation reverses the sign of the imaginary part. Multiplying a number by its conjugate removes its phase and produces a nonnegative real number.

$$z*\  = \ a - ib,\ \ \ \ |z|²\  = \ z*z\  = \ a² + b²$$

- (z+w)\* = z\*+w\*

- (zw)\* = z\*w\*

- \|zw\| = \|z\|\|w\|

- z⁻¹ = z\*/\|z\|² for z ≠ 0

### Worked example 2

For z = 3 + 4i, the modulus is \|z\| = 5. Its inverse is

$$1/z\  = \ (3 - 4i)/25$$

The pattern amplitude times complex-conjugate amplitude will later become central: probabilities and cross sections are built from expressions such as \|M\|².

## 1.4 Polar form and Euler formula

$$eⁱᶿ\  = \ cos\ \theta\  + \ i\ sin\ \theta$$

Every nonzero complex number can be written as z = r e\^(iθ), where r = \|z\| and θ is the argument or phase. Multiplication then multiplies moduli and adds phases; division divides moduli and subtracts phases.

$$(r\ eⁱᶿ)(s\ eⁱᵠ)\  = \ rs\ eⁱ⁽ᶿ⁺ᵠ⁾$$

### Worked example 3

The number 1 + i has modulus √2 and argument π/4, so 1 + i = √2 e\^(iπ/4). Squaring gives 2e\^(iπ/2) = 2i.

## 1.5 Phase and interference

Suppose two alternatives contribute amplitudes A₁ and A₂. The measurable intensity is not usually \|A₁\|² + \|A₂\|²; it is

$$|A₁ + A₂|²\  = \ |A₁|² + |A₂|² + 2\ Re(A₁*A₂)$$

The final term is interference. A relative phase of zero gives reinforcement; a relative phase of π gives cancellation. An overall common phase cancels from the modulus squared, anticipating the physical importance of relative rather than absolute phase.

# 2 Vectors and vector spaces

## 2.1 Abstract vectors

A vector is an object that can be added to another vector and multiplied by a scalar while satisfying the vector-space rules. An arrow in ordinary space is one example, but a polynomial, wave function, spinor, or field configuration can also be a vector. In quantum mechanics the scalars are normally complex numbers.

## 2.2 Coordinates and bases

A basis is an ordered set of linearly independent vectors that spans the space. Once a basis {e₁,...,eₙ} is chosen, a vector v can be represented by a coordinate column.

$$v\  = \ v₁e₁ + \cdots + vₙeₙ\ \  \leftrightarrow \ \ \lbrack v₁\ \ldots\ vₙ\rbrack ᵀ$$

The vector is the abstract object; the column is its representation in a chosen basis. Changing basis changes the components, not the vector.

## 2.3 Linear independence span and dimension

- A set spans a space if every vector in the space is a linear combination of the set.

- A set is linearly independent if the only combination that equals zero has every coefficient equal to zero.

- A basis is both spanning and linearly independent.

- The dimension is the number of elements in any basis of a finite-dimensional space.

### Worked example 4

In ℂ², e₁ = (1,0)ᵀ and e₂ = (0,1)ᵀ form the standard basis. The vectors f₁ = (1,1)ᵀ and f₂ = (1,-1)ᵀ also form a basis because neither is a scalar multiple of the other. The vector v = (3,1)ᵀ becomes v = 2f₁ + f₂.

# 3 Inner products and geometry

## 3.1 The complex inner product

For columns u and v in ℂⁿ, the standard inner product conjugates the first vector.

$$\langle u|v\rangle\  = \ u \dagger v\  = \ \Sigma ⱼ\ uⱼ*\ vⱼ$$

Conjugation guarantees that ⟨v\|v⟩ is real and nonnegative. The inner product is conjugate symmetric: ⟨u\|v⟩ = ⟨v\|u⟩\*. Conventions differ about which slot is linear; physics bra-ket notation is linear in the ket.

## 3.2 Norm orthogonality and normalization

$$\| v\|\  = \ \sqrt{}\langle v|v\rangle$$

Vectors are orthogonal when ⟨u\|v⟩ = 0. A vector is normalized when its norm is one. A basis is orthonormal when every basis vector has unit norm and distinct basis vectors are orthogonal.

### Worked example 5

Let v = (1,i)ᵀ. Then v† = (1,-i), so ⟨v\|v⟩ = 1 + (-i)i = 2. The normalized vector is v/√2.

## 3.3 Completeness in finite dimensions

If {\|eⱼ⟩} is an orthonormal basis, every vector can be reconstructed from its projections.

$$|v\rangle\  = \ \Sigma ⱼ\ |eⱼ\rangle\langle eⱼ|v\rangle,\ \ \ \ \Sigma ⱼ\ |eⱼ\rangle\langle eⱼ|\  = \ I$$

This resolution of the identity later becomes a sum over spin states, polarization states, or intermediate modes.

## 3.4 Gram Schmidt orthonormalization

Given independent vectors v₁ and v₂, normalize the first, subtract from the second its component along the first, and normalize what remains.

$$e₁\  = \ v₁/\| v₁\|,\ \ \ \ u₂\  = \ v₂ - e₁\langle e₁|v₂\rangle,\ \ \ \ e₂\  = \ u₂/\| u₂\|$$

# 4 Linear operators and matrices

## 4.1 Linearity

A map A is linear if A(αu+βv) = αAu+βAv. Once bases are chosen, a linear map is represented by a matrix. Matrix multiplication represents composition of maps; in general AB differs from BA.

## 4.2 Matrix action and composition

$$(Av)ᵢ\  = \ \Sigma ⱼ\ Aᵢⱼvⱼ,\ \ \ \ (AB)ᵢₖ\  = \ \Sigma ⱼ\ AᵢⱼBⱼₖ$$

## 4.3 Identity inverse determinant and trace

  ---------------------------------------------------------------------------------------------------------
  **Object**                          **Meaning**
  ----------------------------------- ---------------------------------------------------------------------
  Identity I                          Iv = v

  Inverse A⁻¹                         A⁻¹A = AA⁻¹ = I

  Determinant det A                   Measures invertibility and oriented volume scaling

  Trace tr A                          Sum of diagonal entries; invariant under similarity transformations
  ---------------------------------------------------------------------------------------------------------

A square matrix is invertible exactly when its determinant is nonzero. For a 2 × 2 matrix,

$$A\  = \ \lbrack a\ b;\ c\ d\rbrack,\ \ \ \ A⁻¹\  = \ (1/(ad - bc))\lbrack d\  - b;\  - c\ a\rbrack$$

## 4.4 Change of basis

Let S have the new basis vectors as its columns, expressed in the old basis. Coordinates transform as \[v\]old = S\[v\]new, and an operator transforms by similarity.

$$\lbrack A\rbrack new\  = \ S⁻¹\lbrack A\rbrack old\ S$$

Similarity changes a matrix representation without changing the underlying linear operator. Trace, determinant, and eigenvalues therefore remain unchanged.

# 5 Eigenvalues eigenvectors and diagonalization

## 5.1 The eigenvalue equation

$$A|v\rangle\  = \ \lambda|v\rangle$$

An eigenvector is a direction whose only change under A is multiplication by λ. Nonzero solutions exist when det(A - λI) = 0. This characteristic equation determines the eigenvalues.

### Worked example 6

For A = \[\[2,1\],\[1,2\]\], the characteristic polynomial is (2-λ)² - 1, giving λ = 3 and λ = 1. Corresponding normalized eigenvectors are (1,1)ᵀ/√2 and (1,-1)ᵀ/√2.

## 5.2 Diagonalization

If an n × n matrix has n independent eigenvectors, put them into the columns of S. Then S⁻¹AS is diagonal, with eigenvalues on the diagonal. Diagonal form makes powers, exponentials, and differential equations easier to compute.

$$A\  = \ S\Lambda S⁻¹\ \  \Rightarrow \ \ f(A)\  = \ Sf(\Lambda)S⁻¹$$

## 5.3 Degeneracy and commuting operators

An eigenvalue is degenerate when more than one independent eigenvector shares it. If two diagonalizable operators commute and suitable regularity conditions hold, one can choose a common eigenbasis. In quantum theory, commuting observables can be assigned simultaneous definite values.

# 6 Adjoint Hermitian and unitary operators

## 6.1 The adjoint

The adjoint A† is the conjugate transpose of a matrix. Abstractly, it is defined by ⟨u\|Av⟩ = ⟨A†u\|v⟩.

- (AB)† = B†A†

- (A†)† = A

- (A⁻¹)† = (A†)⁻¹ when A is invertible

## 6.2 Hermitian operators

$$A \dagger \  = \ A$$

Hermitian operators have real eigenvalues, and eigenvectors belonging to distinct eigenvalues are orthogonal. These facts make Hermitian operators suitable representations of observables.

## 6.3 Unitary operators

$$U \dagger U\  = \ UU \dagger \  = \ I$$

Unitary operators preserve inner products, lengths, angles, and total probability. A change between orthonormal bases is unitary. Time evolution in an isolated quantum system is unitary.

## 6.4 Projectors

$$P²\  = \ P,\ \ \ \ P \dagger \  = \ P$$

For a normalized state \|u⟩, the operator P = \|u⟩⟨u\| projects a vector onto the direction u. Measurement probabilities will be expressed using such projections.

# 7 Bra ket notation

## 7.1 Kets and bras

A ket \|ψ⟩ denotes a vector. Its dual bra ⟨ψ\| is the conjugate transpose. Their product in one order is a scalar and in the reverse order is an operator.

$$\langle\varphi|\psi\rangle\ is\ a\ scalar,\ \ \ \ |\psi\rangle\langle\varphi|\ is\ an\ operator$$

## 7.2 Matrix elements

The scalar ⟨φ\|A\|ψ⟩ is a matrix element of A. It describes how A connects the input state \|ψ⟩ with the output direction \|φ⟩. In QED, scattering amplitudes are built from chains of operators and spinors with exactly this structure.

## 7.3 Expectation values

$$\langle A\rangle\psi\  = \ \langle\psi|A|\psi\rangle,\ \ \ \ \langle\psi|\psi\rangle\  = \ 1$$

For Hermitian A, the expectation value is real. It is an average prediction for repeated measurements on identically prepared systems, not necessarily an eigenvalue from one individual measurement.

# 8 Pauli matrices as a preview of spin

The Pauli matrices act on two-component complex vectors and form the basic algebra of spin one-half. They will reappear in the Dirac equation and in relativistic spinor calculations.

$$\sigma ₓ\  = \ \lbrack 0\ 1;\ 1\ 0\rbrack,\ \ \ \ \sigma ᵧ\  = \ \lbrack 0\  - i;\ i\ 0\rbrack,\ \ \ \ \sigma\_ z\  = \ \lbrack 1\ 0;\ 0\  - 1\rbrack$$

Each Pauli matrix is Hermitian and unitary, has trace zero and determinant -1, and has eigenvalues +1 and -1. Their products satisfy

$$\sigma ᵢ\sigma ⱼ\  = \ \delta ᵢⱼI\  + \ i\ \varepsilon ᵢⱼₖ\sigma ₖ,\ \ \ \ \lbrack\sigma ᵢ,\sigma ⱼ\rbrack\  = \ 2i\ \varepsilon ᵢⱼₖ\sigma ₖ$$

### Worked example 7

The eigenvectors of σ_z are \|+z⟩ = (1,0)ᵀ and \|-z⟩ = (0,1)ᵀ. The +1 eigenvector of σₓ is \|+x⟩ = (1,1)ᵀ/√2. Therefore \|⟨+z\|+x⟩\|² = 1/2: a system prepared with positive x-spin yields either z-spin result with equal probability.

# 9 Connections to QED

  ----------------------------------------------------------------------------------------------------------
  **Mathematical idea**               **Later role in QED**
  ----------------------------------- ----------------------------------------------------------------------
  Complex phase                       Quantum interference and U(1) transformations

  Inner product                       Probabilities, normalizations, and amplitudes

  Linear operator                     Observables, symmetry generators, and propagators

  Eigenvector                         Definite spin, momentum, or energy state

  Unitary map                         Symmetry transformations and quantum evolution

  Hermitian matrix                    Observable or generator with real physical values

  Basis change                        Moving among spin, polarization, position, and momentum descriptions

  Pauli matrices                      Spin algebra and building blocks of Dirac gamma matrices
  ----------------------------------------------------------------------------------------------------------

The local phase transformation at the heart of QED begins with the simple global rule \|ψ⟩ → e\^(iα)\|ψ⟩. Because the factor has unit modulus, inner products and probabilities are unchanged. Requiring invariance when α varies from point to point ultimately forces the introduction of the electromagnetic potential. The algebra learned here is therefore not preliminary decoration; it is part of the mechanism that generates the interaction.

# 10 Summary

1.  Complex numbers encode magnitude and phase; conjugation turns amplitudes into real probabilities.

2.  A vector is independent of its coordinates, while a basis supplies a coordinate representation.

3.  Inner products define norm, angle, orthogonality, and projection.

4.  Matrices represent linear operators; changing basis changes the matrix by similarity.

5.  Eigenvectors identify directions of definite operator action.

6.  Hermitian operators have real eigenvalues; unitary operators preserve inner products.

7.  Bra-ket notation is compact matrix algebra adapted to quantum theory.

8.  The Pauli matrices provide the first concrete model of spin-one-half structure.

# Exercises

  ---------------------------------------------------------------------------------------------------------------------------------------------------------
  **No**                              **Problem**
  ----------------------------------- ---------------------------------------------------------------------------------------------------------------------
  1                                   Compute (2+3i)+(4−i), (2+3i)(4−i), and (2+3i)/(4−i).

  2                                   Write −1+i√3 in polar form using a principal argument in (−π,π\].

  3                                   Show directly that \|zw\|² = \|z\|²\|w\|².

  4                                   Let A₁ = 1 and A₂ = e\^(iφ). Find \|A₁+A₂\|² and evaluate it at φ = 0, π/2, and π.

  5                                   Determine whether (1,i)ᵀ and (i,1)ᵀ are orthogonal in ℂ².

  6                                   Normalize v = (1,1+i,2i)ᵀ.

  7                                   Express (5,1)ᵀ as a combination of f₁=(1,1)ᵀ and f₂=(1,−1)ᵀ.

  8                                   Apply Gram Schmidt to v₁=(1,1)ᵀ and v₂=(1,0)ᵀ.

  9                                   For A=\[\[1,2\],\[3,4\]\], compute det A, tr A, and A⁻¹.

  10                                  Find the eigenvalues and normalized eigenvectors of \[\[4,0\],\[0,−2\]\].

  11                                  Show that eigenvalues of a unitary matrix have modulus one.

  12                                  Show that an expectation value ⟨ψ\|A\|ψ⟩ is real when A is Hermitian.

  13                                  Compute σₓσᵧ and σᵧσₓ, then find \[σₓ,σᵧ\].

  14                                  Find normalized eigenvectors of σᵧ for eigenvalues +1 and −1.

  15                                  Let \|ψ⟩=(cos(θ/2), e\^(iφ)sin(θ/2))ᵀ. Verify normalization and compute ⟨σ_z⟩.

  16                                  Challenge: prove the Cauchy Schwarz inequality \|⟨u\|v⟩\|² ≤ ⟨u\|u⟩⟨v\|v⟩ by considering ‖u−cv‖² with a suitable c.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------

# Solutions

**1.** 6+2i; 11+10i; (5+14i)/17.

**2.** The modulus is 2 and the principal argument is 2π/3, so z=2e\^(2πi/3).

**3.** (zw)\*(zw)=z\*w\*zw=(z\*z)(w\*w), using commutativity of complex multiplication.

**4.** 2+2cosφ. The values are 4, 2, and 0.

**5.** Their inner product is (1,−i)·(i,1)=i−i=0, so they are orthogonal.

**6.** The squared norm is 1+\|1+i\|²+\|2i\|²=7. Thus v/√7 is normalized.

**7.** Solve a+b=5 and a−b=1: a=3 and b=2.

**8.** e₁=(1,1)ᵀ/√2. Subtraction gives u₂=(1/2,−1/2)ᵀ, so e₂=(1,−1)ᵀ/√2.

**9.** det A=−2, tr A=5, and A⁻¹=\[\[-2,1\],\[3/2,−1/2\]\].

**10.** The eigenvalues are 4 and −2, with eigenvectors (1,0)ᵀ and (0,1)ᵀ.

**11.** If Uv=λv, then ‖v‖=‖Uv‖=‖λv‖=\|λ\|‖v‖. For nonzero v, \|λ\|=1.

**12.** Let x=⟨ψ\|A\|ψ⟩. Then x\*=⟨ψ\|A†\|ψ⟩=⟨ψ\|A\|ψ⟩=x, hence x is real.

**13.** σₓσᵧ=iσ_z and σᵧσₓ=−iσ_z, so \[σₓ,σᵧ\]=2iσ_z.

**14.** For +1 use (1,i)ᵀ/√2; for −1 use (1,−i)ᵀ/√2. Overall phases are physically equivalent.

**15.** The norm is cos²(θ/2)+sin²(θ/2)=1. The expectation is cos²(θ/2)−sin²(θ/2)=cosθ.

**16.** For v≠0 choose c=⟨v\|u⟩/⟨v\|v⟩. Expanding 0≤‖u−cv‖² gives ⟨u\|u⟩−\|⟨v\|u⟩\|²/⟨v\|v⟩≥0. Rearrangement proves the claim; v=0 is immediate.

# Mastery checklist

- I can move freely between Cartesian and polar forms of a complex number.

- I automatically conjugate the bra when calculating a complex inner product.

- I can normalize a vector and construct a projector from it.

- I can find eigenvalues and eigenvectors of a 2 × 2 matrix.

- I can test whether a matrix is Hermitian or unitary.

- I can translate simple bra-ket expressions into matrix multiplication.

- I can calculate with Pauli matrices without treating them as mysterious symbols.

# Next lesson

Lesson 2 develops calculus and differential equations, emphasizing derivatives, gradients, Fourier ideas, ordinary differential equations, and the partial differential equations that govern waves and fields.
