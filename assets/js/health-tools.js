/* ToolFest health calculators - browser-only computation */
(function () {
  function byId(id) {
    return document.getElementById(id);
  }

  function num(id, fallback) {
    var el = byId(id);
    if (!el) return fallback;
    var n = parseFloat(el.value);
    return Number.isFinite(n) ? n : fallback;
  }

  function fmt(n, digits) {
    var d = typeof digits === "number" ? digits : 1;
    return n.toLocaleString(undefined, { maximumFractionDigits: d });
  }

  function bmiCategory(v) {
    if (v < 18.5) return "Underweight";
    if (v < 25) return "Healthy range";
    if (v < 30) return "Overweight";
    return "Obesity range";
  }

  function runBmi() {
    var weight = num("weightKg", 70);
    var heightCm = num("heightCm", 170);
    var out = byId("out");
    if (!weight || !heightCm || heightCm <= 0) return;
    var h = heightCm / 100;
    var bmi = weight / (h * h);
    byId("primary").textContent = fmt(bmi, 1);
    byId("secondary").textContent = bmiCategory(bmi);
    out.style.display = "block";
  }

  function runBmrTdee() {
    var sex = byId("sex").value;
    var age = num("age", 30);
    var weight = num("weightKg", 70);
    var heightCm = num("heightCm", 170);
    var activity = parseFloat(byId("activity").value || "1.55");
    var out = byId("out");
    if (!age || !weight || !heightCm || age <= 0 || weight <= 0 || heightCm <= 0) return;
    var bmr;
    if (sex === "female") {
      bmr = 10 * weight + 6.25 * heightCm - 5 * age - 161;
    } else {
      bmr = 10 * weight + 6.25 * heightCm - 5 * age + 5;
    }
    var tdee = bmr * activity;
    byId("primary").textContent = fmt(bmr, 0) + " kcal";
    byId("secondary").textContent = fmt(tdee, 0) + " kcal/day";
    out.style.display = "block";
  }

  function runProtein() {
    var weight = num("weightKg", 70);
    var mult = parseFloat(byId("goal").value || "1.2");
    var out = byId("out");
    if (!weight || weight <= 0) return;
    var protein = weight * mult;
    byId("primary").textContent = fmt(protein, 0) + " g/day";
    byId("secondary").textContent = "at " + mult + " g per kg body weight";
    out.style.display = "block";
  }

  function runDeficit() {
    var maintenance = num("maintenance", 2200);
    var deficit = num("deficit", 500);
    var out = byId("out");
    if (!maintenance || maintenance <= 0) return;
    if (deficit < 0) deficit = 0;
    if (deficit > 1200) deficit = 1200;
    var target = maintenance - deficit;
    if (target < 1200) target = 1200;
    byId("primary").textContent = fmt(target, 0) + " kcal/day";
    byId("secondary").textContent = "from maintenance " + fmt(maintenance, 0) + " kcal/day";
    out.style.display = "block";
  }

  function runMacros() {
    var calories = num("calories", 2200);
    var pCarb = num("carbPct", 40);
    var pProtein = num("proteinPct", 30);
    var pFat = num("fatPct", 30);
    var out = byId("out");
    if (!calories || calories <= 0) return;
    var totalPct = pCarb + pProtein + pFat;
    if (Math.abs(totalPct - 100) > 0.001) {
      byId("primary").textContent = "Adjust ratios to 100%";
      byId("secondary").textContent = "Current total: " + fmt(totalPct, 1) + "%";
      out.style.display = "block";
      return;
    }
    var carbs = (calories * pCarb / 100) / 4;
    var protein = (calories * pProtein / 100) / 4;
    var fat = (calories * pFat / 100) / 9;
    byId("primary").textContent = "C " + fmt(carbs, 0) + "g • P " + fmt(protein, 0) + "g • F " + fmt(fat, 0) + "g";
    byId("secondary").textContent = "for " + fmt(calories, 0) + " kcal/day";
    out.style.display = "block";
  }

  function runWater() {
    var weight = num("weightKg", 70);
    var activity = parseFloat(byId("activity").value || "1");
    var climate = parseFloat(byId("climate").value || "1");
    var out = byId("out");
    if (!weight || weight <= 0) return;
    var ml = weight * 35 * activity * climate;
    var liters = ml / 1000;
    byId("primary").textContent = fmt(liters, 2) + " L/day";
    byId("secondary").textContent = fmt(ml, 0) + " ml total fluids estimate";
    out.style.display = "block";
  }

  function runCurrentTool() {
    var mode = document.body.getAttribute("data-health-tool");
    if (mode === "bmi") runBmi();
    if (mode === "bmr-tdee") runBmrTdee();
    if (mode === "protein") runProtein();
    if (mode === "deficit") runDeficit();
    if (mode === "macros") runMacros();
    if (mode === "water") runWater();
  }

  function wire() {
    var mode = document.body.getAttribute("data-health-tool");
    if (!mode) return;
    var controls = document.querySelectorAll("input, select");
    controls.forEach(function (el) {
      el.addEventListener("input", runCurrentTool);
      el.addEventListener("change", runCurrentTool);
    });
    var cta = byId("calcBtn");
    if (cta) cta.addEventListener("click", runCurrentTool);
    runCurrentTool();
  }

  window.HealthTools = {
    runCurrentTool: runCurrentTool
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", wire);
  } else {
    wire();
  }
})();
