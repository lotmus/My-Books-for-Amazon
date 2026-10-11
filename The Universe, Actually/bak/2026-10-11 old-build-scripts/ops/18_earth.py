# -*- coding: utf-8 -*-
OPS = [
# ---- ch60 exoplanets
('del', 1454, "The observed population includes hot Jupiters"),
('set', 1454, "Atmospheric characterisation is possible", "Atmospheric characterisation is possible for transiting planets. The diversity of architectures found shows that planet formation is robust and that the Solar System is not an inevitable template."),
('sub', 1507, "Water, sodium, potassium, carbon monoxide and methane have been detected.", "Water, sodium, potassium, carbon monoxide and methane are among the species seen."),
('sub', 1507, "The data demonstrate that exoplanet atmospheres span a wide range of metallicities, temperature structures and aerosol properties.", "Strongly irradiated hot Jupiters can develop temperature inversions. The data demonstrate that exoplanet atmospheres span a wide range of metallicities, carbon-to-oxygen ratios, temperature structures and aerosol properties, and that they are not scaled versions of Solar-System atmospheres."),
('delsec', 2204),
('sub', 1503, "The conventional habitable zone is the range of orbital distances at which a rocky planet with an atmosphere can maintain surface liquid water. The boundaries depend on stellar luminosity, planetary albedo and greenhouse strength. For a Sun-like star the zone extends roughly from 0.95 to 1.7 AU.", "The conventional habitable zone, defined in the chapter on the search for life, is only the first filter."),
('sub', 1503, " Occurrence-rate studies show that rocky planets inside habitable zones are common. Whether any of them is inhabited remains an open observational question.", " Whether any rocky planet in a habitable zone is inhabited remains an open observational question."),
# ---- ch61 earth
('set', 1814, "The long-term carbon cycle regulates", "The long-term carbon cycle, described in the section on the carbon-silicate cycle, regulates atmospheric CO₂ on million-year timescales. Perturbations such as large igneous provinces or changes in weathering rates produce excursions recorded in the isotopic composition of sedimentary rocks."),
('set', 1834, "Weathering rates depend on temperature", "Large igneous provinces inject CO₂ faster than weathering can remove it, producing transient warming, while mountain building exposes fresh rock and so increases CO₂ consumption. The isotopic composition of marine carbonates records these imbalances, dates the events and quantifies the size of the perturbations. Geochemical cycles are therefore both regulators and archives of Earth’s surface environment."),
# ---- ch62 climate lead: keep the detailed second half, fold in the Arrhenius sentence
('del', 3352, "The basic mechanism is old and solid."),
('del', 3352, "What has changed is the amount of the gases"),
('del', 3352, "Models are not the foundation."),
('del', 3352, "Impacts scale with the warming."),
('del', 3352, "Climate science is not a mood."),
('sub', 3352, "It is not a model. Models are what you build when you want to know how much, how fast, and where.", "It is not a model. Svante Arrhenius calculated the effect of carbon dioxide in the 1890s, and the calculation has been refined, not repealed. Models are what you build when you want to know how much, how fast, and where."),
('replace', 1802, [
 "Climate science is the study of the long-term statistics of the atmosphere, ocean, cryosphere and land surface, and of the forcings that change those statistics.",
 "Observational records include surface temperature series, satellite radiances, ocean heat content, ice-sheet mass balance and paleoclimate proxies. The instrumental record shows a global surface warming of approximately 1.2 °C since the late nineteenth century. The warming is larger over land than over ocean and larger in the Arctic than in the tropics. Attribution studies using climate models and observations assign the majority of the warming since 1950 to the increase in greenhouse gases from fossil-fuel combustion and land-use change.",
 "Models solve the fluid equations on a rotating sphere together with radiation, convection and cloud parameterisations. Equilibrium climate sensitivity to a doubling of CO₂ lies between 2 °C and 5 °C, and regional changes in precipitation, extremes and sea level follow. The physical basis is established; the remaining uncertainties are quantitative.",
]),
('sub', 1427, " The equilibrium climate sensitivity to a doubling of carbon dioxide is estimated between 2 K and 5 K.", ""),
# ---- ch63 ecology
('delsec', 1372),
]
