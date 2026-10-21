---
id: "636e7df454e220ff"
title: "vale la pena un verificador independiente o es puro gasto de mas"
url: "https://reddit.com/r/artificial/comments/1xb2xku/vale_la_pena_un_verificador_independiente_o_es"
link: "https://reddit.com/r/artificial/comments/1xb2xku/vale_la_pena_un_verificador_independiente_o_es"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T20:15:40Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["1982_miguel"]
language: "en"
summary: "Buenas, aca dandole vueltas a un problema de diseño en sistemas con agentes de IA y queria saber su opinion o si alguien ha implementado algo asi en produccion....que herramientas comunes se utilizan,framework,librerias, skill muy detallados, algun mcp etc. Me pasa seguido que cuando un agente ejecuta tareas complejas, al final declara que la tarea esta completada (\"task completed\", todo verde),…"
tags: ["r/artificial"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 346
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xb2xku/vale_la_pena_un_verificador_independiente_o_es/"
score: null
comments: null
community: "r/artificial"
---

# vale la pena un verificador independiente o es puro gasto de mas

Reddit · 1982_miguel · 2026-10-20

Buenas, aca dandole vueltas a un problema de diseño en sistemas con agentes de IA y queria saber su opinion o si alguien ha implementado algo asi en produccion....que herramientas comunes se utilizan,framework,librerias, skill muy detallados, algun mcp etc. Me pasa seguido que cuando un agente ejecuta tareas complejas, al final declara que la tarea esta completada ("task completed", todo verde), pero cuando miras el detalle te das cuenta que en el camino se salto reglas de negocio o dio por bueno algo que no era. La solucion tipica que veo es meterle un buen prompt o un Skill muy detallado de autochequeo al mismo modelo para que revise su propia respuesta antes de entregarla. Pero me da la impresion de que cae en un sesgo de confirmacion gigante (si se equivoco al ejecutar, se suele equivocar igual al auditarse a si mismo). Un ejemplo super simple para graficarlo: Imagina que subes un contrato de 40 paginas a Claude y le preguntas "cumple con todos los requisitos?". Claude te dice feliz "Si, cumple todo". Pero resulta que las bases pedian una garantia de $5.000.000 y el documento venia con una de $3.000.000. Claude te la vendio y te dijo que estaba bien igual. Ahi es donde entra la duda de si conviene armar un verificador independiente (un modelo mas chico, reglas deterministas en codigo, o un flow hibrido) que no busque ser "mas inteligente", sino comprobar sistematicamente requisito por requisito. Tipo un output asi: Plazo de entrega: Exigido 30 dias / Propuesto 25 dias -> Cumple. Garantia: Exigida $5.000.000 / Encontrada $3.000.000 -> No cumple. Experiencia minima: Sin evidencia suficiente -> Requiere revision manual. O sea, pasar de una respuesta convincente a una revision comprobable punto por punto. Entonces mi duda de fondo para el debate es: realmente puede un verificador independiente detectar estas infracciones durante la ejecucion con mayor precision que el mismo modelo usando un buen Skill, y con un costo/latencia extra lo suficientemente bajo como para que valga la pena en la practica? O al final el gasto extra de tokens no compensa?
