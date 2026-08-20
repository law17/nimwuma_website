---
layout: page
title: "Pricing"
eyebrow: "Clear starting points"
intro: "Ghana services are priced in Ghana cedis. Standard global services are priced in US dollars."
description: "Pricing for Ghana Business Operations and Global Operations services."
---

<h2 id="ghana">Ghana Businesses</h2>
<p>{{ site.data.pricing.ghana.note }}</p>
<div class="pricing-grid">
{% for plan in site.data.pricing.ghana.plans %}
  {% include pricing-card.html plan=plan symbol=site.data.pricing.ghana.symbol %}
{% endfor %}
</div>

Package allowances and onboarding requirements vary by service. Historical record cleanup and material work outside an agreed package are quoted separately.

<h2 id="global">Global Businesses</h2>
<p>{{ site.data.pricing.global.note }}</p>
<div class="pricing-grid">
{% for plan in site.data.pricing.global.plans %}
  {% include pricing-card.html plan=plan symbol=site.data.pricing.global.symbol %}
{% endfor %}
</div>

Global pricing is a starting point. Complex workflows, unusual service hours, specialist knowledge, regulated activities or managed multi-person teams may require a tailored quotation.
