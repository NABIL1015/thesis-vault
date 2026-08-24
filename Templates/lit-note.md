---
title: "{{title}}"
citekey: {{citekey}}
authors: [{% for a in creators %}"{{a.lastName}}"{% if not loop.last %}, {% endif %}{% endfor %}]
year: {{date | format("YYYY")}}
category: ""
aliases: ["{{citekey}}"{% for a in creators %}, "{{a.lastName}}"{% endfor %}]
tags: [literature]
tau1_value: ""
tau1_units: ""
tau2_value: ""
nondim_convention: ""
airfoil: ""
reynolds: ""
config: ""
version_held: ""
version_to_cite: ""
doi: "{{DOI}}"
---

## {{title}}

**Full citation:** {{bibliography}}

### One-line contribution


### Key equations


### Reported parameter values
- τ₁ = 
- τ₂ = 

### My annotations
{% persist "annotations" %}
{% for annotation in annotations %}
> {{annotation.annotatedText}}
{% if annotation.comment %}— {{annotation.comment}}{% endif %}
{% endfor %}
{% endpersist %}
