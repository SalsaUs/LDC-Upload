/* ==========================================================
   Land Development Consultants – site scripts
   1. Mobile menu toggle
   2. Quote form: validate, then send to Formspree (emails the enquiry)
   3. Footer year
   Loaded on every page. The directory filter and the "List your business"
   form scripts are small inline scripts written by dir_pages.py.
   The enquiry form relies on these ids: quote, service, suburb, email, form-msg.
   ========================================================== */

// --- 1. Mobile menu -------------------------------------------------
const menuBtn = document.querySelector(".menu-btn");
const nav = document.getElementById("nav");

menuBtn.addEventListener("click", () => {
  const open = nav.classList.toggle("open");
  menuBtn.setAttribute("aria-expanded", String(open)); // keeps screen readers informed
});
// Close the menu after tapping a link
nav.addEventListener("click", (e) => {
  if (e.target.tagName === "A") {
    nav.classList.remove("open");
    menuBtn.setAttribute("aria-expanded", "false");
  }
});

// --- 2. Quote form --------------------------------------------------
// Sends the enquiry to Formspree, which emails it to you.
// The form's action URL is set in index.html.
const form = document.getElementById("quote");
const msg = document.getElementById("form-msg");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const data = new FormData(form);
  const email = (data.get("email") || "").trim();

  // Basic checks with plain-language messages
  if (!data.get("service") || !(data.get("suburb") || "").trim() || !/^\S+@\S+\.\S+$/.test(email)) {
    msg.textContent = "Please choose a service and enter your suburb and a valid email.";
    msg.classList.add("error");
    return;
  }
  msg.classList.remove("error");
  msg.textContent = "Sending…";

  try {
    // Send the form data to Formspree in the background (no page reload)
    const res = await fetch(form.action, {
      method: "POST",
      body: data,
      headers: { Accept: "application/json" }
    });
    if (res.ok) {
      form.reset();
      msg.textContent = "Thanks! We've received your enquiry and will be in touch soon.";
    } else {
      throw new Error("Server error");
    }
  } catch (err) {
    msg.textContent = "Sorry, something went wrong. Please try again in a moment.";
    msg.classList.add("error");
  }
});

// --- 3. Footer year -------------------------------------------------
document.getElementById("year").textContent = new Date().getFullYear();

