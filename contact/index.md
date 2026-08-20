---
layout: page
title: "Talk to"
title_brand: true
eyebrow: "Start with the problem"
intro: "Tell us where operational work is consuming your time and what you need help managing."
---

<div class="contact-grid">
<div>
<h2>What happens next?</h2>
<p>We will first understand the work you want to delegate, the approximate volume, the systems involved and the decisions that must remain with your team.</p>
{% if site.data.company.contact.email_active %}
<p>Enquiries can be sent to <a href="mailto:{{ site.data.company.contact.email }}">{{ site.data.company.contact.email }}</a>.</p>
{% else %}
<p class="notice"><strong>Staging site:</strong> the public business email will be added after the domain and mailbox are secured.</p>
{% endif %}
</div>
<div class="contact-card">
<h2>Useful information to include</h2>
<ul>
<li>Your business and country</li>
<li>Whether you need Ghana Business Operations or Global Operations</li>
<li>The recurring work you want help with</li>
<li>Approximate task, customer or transaction volume</li>
<li>Any systems {{ site.data.company.brand.name }} would need to work with</li>
<li>Your preferred start timeframe</li>
</ul>
{% if site.data.company.contact.email_active %}
<a class="button" href="mailto:{{ site.data.company.contact.email }}?subject=Service%20enquiry">Email {{ site.data.company.brand.name }}</a>
{% else %}
<p class="muted">Direct enquiries will open when the business mailbox is activated.</p>
{% endif %}
</div>
</div>
