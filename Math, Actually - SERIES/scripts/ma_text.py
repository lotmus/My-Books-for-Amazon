# -*- coding: utf-8 -*-
"""Authored text and data for the Math, Actually build."""
AUTHOR = 'Lothar J. Musiol'

VOLUMES = {
 1: dict(subtitle='From Arithmetic to Calculus', chapters=(1, 12),
         keywords='arithmetic; algebra; functions; geometry; trigonometry; logarithms; vectors; limits; calculus',
         blurb='Counting and number theory, algebra, functions and graphs, coordinates, Euclidean geometry, trigonometry, logarithms, systems of equations, vectors, limits, the derivative, and the integral. Chapters 1–12; it reads on its own through single-variable calculus.'),
 2: dict(subtitle='From Multivariable Calculus to Set Theory & Logic', chapters=(13, 25),
         keywords='multivariable calculus; vector calculus; series; Fourier; Laplace; linear algebra; complex analysis; set theory',
         blurb='Multivariable functions and calculus, vector calculus, series, Fourier and Laplace transforms, integral geometry, matrices, linear algebra, analytic geometry, complex analysis, counting, and set theory and logic. Chapters 13–25.'),
 3: dict(subtitle='From Differential Equations to Abstract Algebra', chapters=(26, 37),
         keywords='differential equations; PDE; optimization; numerical methods; differential geometry; topology; manifolds; functional analysis; measure theory; abstract algebra',
         blurb='Differential and integro-differential equations, partial differential equations, optimization and the calculus of variations, numerical methods, differential geometry, topology, advanced integral geometry, tensors and manifolds, functional analysis, measure theory, and abstract algebra. Chapters 26–37.'),
 4: dict(subtitle='From Category Theory to the Frontier', chapters=(38, 50),
         keywords='category theory; information theory; wavelets; game theory; statistics; probability; control theory; chaos; mathematical physics; modeling',
         blurb='Category theory, information theory, wavelets, game theory, statistics and probability, computational geometry, control theory, dynamical systems and chaos, mathematical physics, advanced optimization and numerical methods, and mathematical modeling. Chapters 38–50.'),
}

CHAPTER_TITLE_FIX = {50: 'Where Mathematics Meets the World'}

TOPIC_OVERRIDE = {}

ALSO_BY = ('Also by Lothar J. Musiol: *Physics, Actually*, the companion series on the physical world, '
           'and *Quanta, Actually*, on the quantum world. Every title is listed on the Also by Lothar J. Musiol '
           'page at the back of this volume.')

# Back matter: the canonical 'Also by Lothar J. Musiol' list (same in every book; see
# notes/ALSO_BY - canonical list.md at the repo root). Titles as on each master's title page.
ALSO_BY_HEADING = 'Also by Lothar J. Musiol'
ALSO_BY_LIST = [
    ('Physics, Actually', [
        'Physics, Actually, Volume 1: Motion, Forces, Time, and Relativity',
        'Physics, Actually, Volume 2: Gravity, Cosmology, and the Limits of Spacetime',
        'Physics, Actually, Volume 3: The Standard Model, Chaos, and the Edge of Knowledge',
        'Life, Actually: From the First Cell to the Edited Genome and the Search for Life Elsewhere',
    ]),
    ('Math, Actually', [
        'Math, Actually, Volume 1: From Arithmetic to Calculus',
        'Math, Actually, Volume 2: From Multivariable Calculus to Set Theory & Logic',
        'Math, Actually, Volume 3: From Differential Equations to Abstract Algebra',
        'Math, Actually, Volume 4: From Category Theory to the Frontier',
    ]),
    ('Quanta, Actually', [
        'Quanta, Actually, Volume 1: The Quantum World',
        'Quanta, Actually, Volume 2: The Quantum Conversation',
        'Quanta, Actually, Volume 3: Complete Quantum Electrodynamics Course',
    ]),
    ('Science Sparks', [
        'Science Sparks: Physics, Life, and Mathematics — The Same Few Rules, Told in Highlights',
    ]),
    ('Look First', [
        'Look First, Volume 1: The Universe Has No Now',
        'Look First, Volume 2: A Trip Is Not a New Life',
    ]),
    ('Electrical Engineering Series', [
        'Foundations of Electronics (Book 1)',
        'Circuits, Components, and Control (Book 2)',
        'Semiconductor Physics and Devices (Book 3)',
        'RF, Microwave, and Transceivers (Book 4)',
        'Communications, Wireless, and SDR (Book 5)',
        'Power and Energy (Book 6)',
        'Packaging, Layout, EMC, and Test (Book 7)',
    ]),
    ('History', [
        "The Dolphins' View of History",
    ]),
    ('Fiction', [
        "The Murder That Hadn't Happened Yet (The Relativistic Investigation Bureau, Book 1)",
        'The Warning That Was Sent Too Late (The Relativistic Investigation Bureau, Book 2)',
        'Schrödinger’s Paperwork (Lolly Wren’s Curious Science Adventures, Book 1)',
        'The Permitted Options (Lolly Wren’s Curious Science Adventures, Book 2)',
        'Protocol Flamingo (The Invasion Storybooks, Book 1), as George Herbert Fontaine',
    ]),
    ('How-To', [
        'Your First Book That Sells',
        'Your First YouTube Channel That Rocks',
    ]),
]

def front_titles(vol):
    return ['Preface'] if vol == 1 else ['About This Volume']

def preface(vol):
    if vol == 1:
        return [('h1', 'Preface'),
 ('p', 'Welcome to *Math, Actually*. This is one book about mathematics, published as four volumes because no single spine could hold it: fifty chapters, from counting to the research frontier, written to be read in order or dipped into where you need them. The chapters began as separate manuscripts, each once content to stand alone on a shelf with its own index and its own faintly apologetic preface. They have been joined into one continuous text. Where one book used to end with a full stop and a wave goodbye, a chapter now hands its ideas straight to the next. Mathematics was never a row of unrelated courses, and pretending otherwise, one marketing budget per course, was a small and forgivable lie that has now been tidied up.'),
 ('p', 'The reason for doing it this way is that mathematics is a single connected structure pretending, for administrative convenience, to be several hundred unconnected ones. You cannot do calculus without algebra underneath it; you cannot do functional analysis without calculus, linear algebra, and a worrying amount of measure theory beneath that. Splitting these into fifty standalone books was good for the shelf and bad for the truth. Each idea in this series rests on ideas met earlier, and the text says so, with a link, every time it leans on one.'),
 ('p', 'How you read it is entirely up to you, and I say this as someone who has spent an unreasonable fraction of one career telling undergraduates how to read things. You may start at Chapter 1, with arithmetic — genuinely, properly, from the beginning, counting on your fingers if it comes to that — and read straight through to the mathematical physics and applied modeling at the end of Volume 4. That is the recommended route for anyone with patience, several free years, and no pressing deadline. It is also the route that makes each new chapter easy, because nothing is asked of you before it has been built.'),
 ('p', 'Alternatively — and this is the route most people will take, so let us not pretend otherwise — you may go directly to the chapter you need. Revising trigonometry before an exam? Chapter 6. Trying to remember what a Fourier transform is for, as opposed to what it is? Chapter 17. Wandered in from an engineering problem and need control theory by Tuesday? Chapter 45, and good luck. Every chapter tells you at the start what it assumes, and every section that uses an earlier idea links back to the place where that idea was introduced, so dipping in does not feel like arriving at a dinner party in the middle of an argument nobody explained.'),
 ('p', 'The layout is simple. Each chapter covers one broad territory — arithmetic, geometry, topology, and so on — and each section within it covers one idea: factoring, the chain rule, compactness. Sections are numbered by chapter, so Section 11.4 is the fourth section of Chapter 11. Some sections are short and get you in and out in a few paragraphs. Others — measure theory, I am looking at you — run rather longer than their titles suggest, and I can only apologize on behalf of the subject, not the author.'),
 ('p', 'I should confess that the later chapters contain ideas that took the human species several centuries and a fair number of nervous breakdowns to work out, and that I have compressed them into sections you can read over a cup of tea. This is either a great service to civilization or a mild insult to the mathematicians who did the actual suffering, and I have chosen not to dwell on which. Infinity in particular gets a great deal of attention, and I will say now what I will say again later at greater length: it does not behave, it does not apologize, and it has outlasted every mathematician who has ever tried to tame it.'),
 ('p', 'You will find, at regular intervals, worked examples — proper ones, with real numbers where real numbers will do, and honest concrete instances where the idea is too structural for arithmetic to touch. This is not decoration. An idea you cannot compute with is an idea you do not yet own, however elegantly you can recite it at a dinner party. Every one of these examples has been checked by hand, more than once, because a mathematics book that gets its own arithmetic wrong is a special and particular kind of disgrace.'),
 ('p', 'Every section follows the same order. It opens in plain language — what the idea is, why anyone wanted it, and what it feels like — before any formula appears. Then come the definitions and equations, and then the worked examples that put them to use. What follows is not a shortcut through mathematics; there isn’t one, whatever the adverts for certain revision guides may imply. It is, I hope, an honest route, with the steps cut small and nothing left unexplained. Chapter 1 starts, appropriately enough, with counting.'),
        ]
    prev = {2: 'Volume 1 (Chapters 1–12) runs from arithmetic to single-variable calculus and holds the full preface.',
            3: 'Volume 1 (Chapters 1–12) runs from arithmetic to single-variable calculus and holds the full preface; Volume 2 (Chapters 13–25) extends calculus to many variables and adds transforms, linear algebra, complex analysis, and the foundations of mathematics.',
            4: 'Volume 1 (Chapters 1–12) begins at arithmetic and holds the full preface; Volume 2 (Chapters 13–25) extends calculus to many variables and lays the foundations in set theory and logic; Volume 3 (Chapters 26–37) covers differential equations, geometry, analysis, and abstract structure.'}[vol]
    this = {2: 'This volume covers Chapters 13 through 25: multivariable and vector calculus, series and integral transforms, matrices and linear algebra, analytic and integral geometry, complex analysis, counting and discrete mathematics, and set theory and logic. Thirteen chapters that take everything Volume 1 built in one variable and generalize it — more dimensions, more structure, and, by the end, a first proper look at the foundations mathematics itself stands on.',
            3: 'This volume covers Chapters 26 through 37: differential, integro-differential, and partial differential equations; optimization and the calculus of variations; numerical methods; differential geometry, topology, and advanced integral geometry; tensors and manifolds; functional analysis; measure theory; and abstract algebra. Twelve chapters about the equations that describe change, and the increasingly abstract structures mathematicians built to solve, generalize, and finally justify them.',
            4: 'This volume covers Chapters 38 through 50: category theory; information theory; wavelets and signal analysis; game theory and decision mathematics; statistics and probability, in their standard and advanced forms; computational geometry; control theory; dynamical systems and chaos; mathematical physics; advanced optimization; advanced numerical methods; and mathematical modeling. Thirteen chapters, from the most abstract structures in the whole series to the discipline that points all of it back at the physical world.'}[vol]
    link = {2: 'Volume 1 ended with the integral. This volume opens by asking what happens to the derivative and the integral when a function depends on more than one number, and it closes with the logic and set theory on which every earlier chapter quietly relied. Volume 3 takes up differential equations, optimization, and the geometry that holds them together.',
            3: 'Volume 2 ended with set theory and logic, quietly underwriting everything before it. This volume opens with differential equations, which put the calculus of Volumes 1 and 2 to work on change itself, and it closes with abstract algebra. Volume 4 picks up where abstract algebra leaves off, with category theory, and continues to the research frontier.',
            4: 'Volume 3 ended with abstract algebra. This volume opens with category theory, the language that describes what all of those structures have in common, and it closes where the series has been heading from the first page: mathematics put to work on the world.'}[vol]
    return [('h1', 'About This Volume'),
            ('p', f'This is Volume {vol} of *Math, Actually*, one continuous fifty-chapter book about mathematics published in four volumes. {prev} If this is your first volume, the short notes that follow explain how the book is organized and where its foundations are; references to earlier volumes are given as a topic name with its volume, for example “Limits (Volume 1)”.'),
            ('p', this), ('p', link)]

def organized(vol):
    return [('h1', 'How This Book Is Organized'),
 ('p', 'The fifty chapters of *Math, Actually* run continuously across the four volumes, so Chapter 13 opens Volume 2 and Chapter 50 closes Volume 4. Each chapter is one broad territory of mathematics. Each section within a chapter is one idea, numbered by its chapter: Section 6.3 is the third section of Chapter 6. Each chapter ends with Check Your Understanding questions and a set of Problems; their answers are at the back of the volume.'),
 ('p', 'Whenever a section uses an idea from somewhere else, it names that section by its topic. Inside this volume the name is a link: follow it and you land on the section, and the Back button of your reader brings you home again. An idea from another volume cannot be linked across files, so it is named with its volume instead — “Limits (Volume 1)” — and the Subject Index of that volume will find it.'),
 ('p', 'Every section is built in the same order. It opens in plain language: what the idea is, why it matters, and what it feels like, usually with numbers you can check by hand. The definitions and formulas come next, once you have seen why they are needed. The worked examples follow and put the formulas to use.'),
 ('p', 'One more convention, purely visual. Worked examples appear in shaded boxes rather than running paragraphs, so that your eye can find them again on a later skim. A blue box marks an example that works through actual numbers, or through the general case when numbers would not illuminate anything — either way, one clean argument from start to finish. A purple box marks the rarer case where you get both: the concrete instance and the general pattern beside it, on the theory that seeing the same idea twice, once with numbers and once without, is worth the extra half-page far more often than authors like to admit.'),
    ]

def foundations(vol):
    return [('h1', 'Where the Foundations Are'),
 ('p', 'One structural confession, best made early. The book begins with counting, because that is where a human being begins. But the logical foundations of mathematics — the axioms of set theory, the rules of inference, the machinery that says what a proof is — are not in Chapter 1. They are in Chapter 25, at the end of Volume 2, which is an odd place to put a foundation.'),
 ('p', 'This is deliberate, and it is not a compromise. Mathematics was not discovered in logical order. Counting is some tens of thousands of years old; the axioms that justify it were written down in the 1920s. Children learn arithmetic long before they learn what a set is, and the ones who go on to learn what a set is do not thereby discover that their arithmetic was wrong. The foundations were laid underneath a subject that was already well established and doing perfectly well.'),
 ('p', 'So you do not need Chapter 25 to read the chapters before it. You will want to read it eventually, for the same reason anyone eventually looks at foundations: not because anything is falling down, but because you have started to wonder what is holding it all up. Readers who prefer their logic first are welcome to read Chapter 25 early. It assumes very little and says so.'),
    ]

EPILOGUE_TITLE = {1: 'Epilogue — Halfway Through the Calculus', 2: 'Epilogue — Between Volumes',
                  3: 'Epilogue — Between Volumes', 4: 'Epilogue — Looking Back over the Whole'}
EPILOGUE = {
 1: ['This is a pause, not the end. The book continues in Volume 2.',
     'It is worth pausing here anyway. You have read twelve chapters, and they are the ones everything later leans on — which means the effort you have already spent is about to start paying compound interest. Mathematics punishes the reader who meets an idea cold and rewards the one who has met it before, however briefly. You now have a great many such half-memories, and every one of them is a hook that later reading can hang on.',
     'Before going on, consider going back to the one chapter that nagged at you. A second reading of mathematics is worth roughly four first readings, and the difference is almost entirely that you are no longer spending effort on the vocabulary.',
     'When you are ready, Volume 2, *From Multivariable Calculus to Set Theory & Logic*, takes up functions of several variables, the transforms, linear algebra, complex analysis, and the foundations in set theory and logic. It begins exactly where Chapter 12 stopped: with the integral, now asked to work in more than one dimension.'],
 2: ['This is a pause, not the end. The book continues in Volume 3.',
     'You have now read twenty-five chapters. Calculus has been taken into many dimensions, linear algebra has turned systems of equations into geometry, complex analysis has shown how much a single derivative can know, and the last chapter dug down to the logic underneath all of it. That is the toolkit almost every later chapter will reach for.',
     'Before going on, consider rereading the chapter that resisted you. Linear algebra in particular repays a second pass more generously than almost anything else in mathematics.',
     'When you are ready, Volume 3, *From Differential Equations to Abstract Algebra*, opens with differential equations — calculus put to work on change itself — and moves through optimization, geometry, analysis, and measure theory to abstract algebra.'],
 3: ['This is a pause, not the end. The book continues in Volume 4.',
     'Thirty-seven chapters are behind you. Differential equations, optimization, numerical methods, geometry, topology, functional analysis, measure theory, and abstract algebra are the working language of most of modern mathematics, and you have now met all of them at least once.',
     'Before going on, consider rereading the chapter that resisted you. Measure theory and functional analysis in particular read very differently the second time, once you know where they are going.',
     'When you are ready, Volume 4, *From Category Theory to the Frontier*, opens with category theory — the language that describes what all of these structures have in common — and ends with mathematics put to work on the world.'],
 4: ['This is the end of the book, and it is worth a moment.',
     'Fifty chapters ago you were counting sheep with tally marks. Since then you have built the numbers, learned to solve for what you do not know, measured change and accumulation, taken calculus into many dimensions, solved the equations of change, met the abstract structures that organize all of it, and finally turned the whole apparatus back on the world — on signals, games, data, machines, and physical law. Nothing in that sequence was assumed before it had been built.',
     'None of it is finished. Every chapter of this book is the front edge of a field that is still growing, and the Further Reading appendix names the books that will take you further in any direction you choose. The point of a survey was never to be the last word. It was to make sure that when you open one of those books, nothing in it is wholly unfamiliar.',
     'Go back to the chapter that surprised you most. Then pick up a pencil.'],
}
CLOSING = {
 1: ['If this volume made you see something ordinary — a remainder, a slope, an area — a little differently, it did its job. Volume 2 is waiting when you are.', 'Thank you for reading.'],
 2: ['If this volume made you see something ordinary — a weather map, a sound wave, a set — a little differently, it did its job. Volume 3 is waiting when you are.', 'Thank you for reading.'],
 3: ['If this volume made you see something ordinary — a cooling cup of tea, a soap film, a symmetry — a little differently, it did its job. Volume 4 is waiting when you are.', 'Thank you for reading.'],
 4: ['If this book made you see something ordinary — a coin toss, a thermostat, a weather forecast — a little differently, it did its job. *Physics, Actually* and *Life, Actually* take the same approach to the physical world and to living things.', 'Thank you for reading all fifty chapters.'],
}

LITERAL = {}   # filled by literal_fixes.py if present

def literal_fixes(vol):
    try:
        import literal_fixes as L
        return L.FIXES.get(0, []) + L.FIXES.get(vol, [])
    except ImportError:
        return []
