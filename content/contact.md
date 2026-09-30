---
title: "Contact Us"
type: "page"
description: "Contact the Jaipuria College editorial desk."
---

Have a correction, a news tip or feedback about our coverage? Send us a message using the form below.

<form class="contact-form" id="contactForm">
  <label for="cf-name">Your name</label>
  <input id="cf-name" name="name" type="text" required autocomplete="name">

  <label for="cf-email">Email address</label>
  <input id="cf-email" name="email" type="email" required autocomplete="email">

  <label for="cf-msg">Message</label>
  <textarea id="cf-msg" name="message" rows="6" required></textarea>

  <button type="submit">Send message</button>
  <p class="form-note">This form is front-end only for now; our contact backend is being connected. For urgent corrections, please mention the article URL in your message.</p>
  <p class="form-ok" id="cf-ok" hidden>Thanks. Your message has been recorded. We read every message.</p>
</form>

<script>
document.getElementById('contactForm').addEventListener('submit', function (e) {
  e.preventDefault();
  var ok = document.getElementById('cf-ok');
  ok.hidden = false;
  this.querySelector('button').disabled = true;
  ok.scrollIntoView({ behavior: 'smooth', block: 'center' });
});
</script>
