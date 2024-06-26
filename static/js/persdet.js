const subjects = {
  science: [
    "Physics",
    "Chemistry",
    "Biology",
    "Mathematics",
    "Computer Science",
    "Biotechnology",
    "Environmental Science",
    "Geology",
    "Astronomy",
    "Statistics",
    "Agriculture Science",
    "Electronics",
    "Psychology",
    "Home Science",
    "Geography",
    "Engineering Drawing",
    "Nutrition and Dietetics",
    "Forensic Science",
    "Industrial Chemistry",
    "Bioinformatics",
    "Anthropology",
    "Sociology",
    "Home Economics",
    "Applied Mathematics",
    "Biochemistry",
    "Microbiology",
    "Genetics",
    "Pharmacology",
    "Oceanography",
    "Physics with Astrophysics",
    "Food Technology",
    "Polymer Science",
    "Textile Technology",
    "Meteorology",
    "Immunology",
    "Nanotechnology",
    "Remote Sensing",
    "Virology",
    "Biophysics",
    "Applied Geology",
    "Animal Husbandry and Veterinary Science",
    "Horticulture",
    "Dairy Technology",
    "Fisheries Science",
    "Sericulture",
    "Aquaculture",
    "Forestry",
    "Entomology",
    "Plant Pathology",
    "Agronomy",
    "English",
    "Hindi",
    "Sanskrit",
    "Bengali",
    "Telugu",
    "Marathi",
    "Tamil",
    "Urdu",
    "Gujarati",
    "Kannada",
    "Odia",
    "Punjabi",
  ],
  commerce: [
    "Accountancy",
    "Business Studies",
    "Economics",
    "Entrepreneurship",
    "Mathematics (optional)",
    "Informatics Practices (optional)",
    "Statistics (optional)",
    "Finance",
    "Marketing",
    "Human Resource Management",
    "Financial Management",
    "Cost Accounting",
    "Company Law",
    "Auditing",
    "Taxation",
    "Banking and Insurance",
    "International Business",
    "Retail Management",
    "Supply Chain Management",
    "Financial Markets",
    "Business Communication",
    "Organizational Behavior",
    "Management Accounting",
    "Business Law",
    "Corporate Governance",
    "E-commerce",
    "Risk Management",
    "Investment Management",
    "Strategic Management",
    "Public Finance",
    "Microeconomics",
    "Macroeconomics",
    "English",
    "Hindi",
    "Sanskrit",
    "Bengali",
    "Telugu",
    "Marathi",
    "Tamil",
    "Urdu",
    "Gujarati",
    "Kannada",
    "Odia",
    "Punjabi",
  ],
};

function generateSubjectRow(labelNumber, subjectOptions, index) {
  return `<div class="form-row subject-row">
                    <div class="col-md-6 mb-3">
                        <label>Subject ${labelNumber}</label>
                        <select class="form-control subject-select"  name="twelfth_subject${index}" required>
                            <option value="" selected disabled>Select Subject</option>
                            ${subjectOptions}
                        </select>
                    </div>
                    <div class="col-md-3 mb-3">
                        <label>Marks Obtained</label>
                        <input type="number" class="form-control marks-obtained" placeholder="Marks" name="twelfth_subject${
                          index + 1
                        }_marks_obtained" required>
                    </div>
                    <div class="col-md-3 mb-3">
                        <label>Total Marks</label>
                        <input type="number" class="form-control max-marks" placeholder="Total" name="twelfth_subject${
                          index + 1
                        }_total_marks" value="100" required>
                    </div>
                </div>`;
}

function addSubjectRows(subjectType) {
  const subjectRowsContainer = $("#subjectRows");
  subjectRowsContainer.empty();
  const selectedSubjects = subjects[subjectType];
  for (let i = 0; i < 5; i++) {
    const subjectOptions = selectedSubjects
      .map((subject) => `<option value="${subject}">${subject}</option>`)
      .join("");
    const subjectRowHTML = generateSubjectRow(i + 1, subjectOptions, i + 1);
    subjectRowsContainer.append(subjectRowHTML);
  }
  if (subjectType=="science"){

  document.getElementById("coursePrefernce").innerHTML=`<h5 style="text-align: center;">Course Preference</h5>
  <hr class="hr border-dark"><div class="form-row subject-row">
  <div class="col-md-6 mb-3">
      <label>Preference 1</label>
      <select class="form-control preference-select"  name="preference1" required>
          <option value="" selected disabled>Select Choice</option>
          <option value="Software Systems">Software Systems</option>
          <option value="Data Science">Data Science</option>
          <option value="Artificial Intelligence and Machine Learning">Artificial Intelligence and Machine Learning</option>
          <option value="Decision and Computing Science">Decision and Computing Science</option>
      </select>
  </div>
  <div class="col-md-6 mb-3">
  <label>Preference 2</label>
  <select class="form-control preference-select"  name="preference2" required>
      <option value="" selected disabled>Select Choice</option>
      <option value="Software Systems">Software Systems</option>
      <option value="Data Science">Data Science</option>
      <option value="Artificial Intelligence and Machine Learning">Artificial Intelligence and Machine Learning</option>
      <option value="Decision and Computing Science">Decision and Computing Science</option>
  </select>
  </div>
  <div class="col-md-6 mb-3">
  <label>Preference 3</label>
  <select class="form-control preference-select"  name="preference3" required>
      <option value="" selected disabled>Select Choice</option>
      <option value="Software Systems">Software Systems</option>
      <option value="Data Science">Data Science</option>
      <option value="Artificial Intelligence and Machine Learning">Artificial Intelligence and Machine Learning</option>
      <option value="Decision and Computing Science">Decision and Computing Science</option>
  </select>
  </div>
  <div class="col-md-6 mb-3">
  <label>Preference 4</label>
  <select class="form-control preference-select"  name="preference4" required>
      <option value="" selected disabled>Select Choice</option>
      <option value="Software Systems">Software Systems</option>
      <option value="Data Science">Data Science</option>
      <option value="Artificial Intelligence and Machine Learning">Artificial Intelligence and Machine Learning</option>
      <option value="Decision and Computing Science">Decision and Computing Science</option>
  </select>
  </div>
</div>`
}
else{
  document.getElementById("coursePrefernce").innerHTML=
  
  `<div style="display:none"><select class="form-control preference-select"  name="preference1">
  <option value="Decision and Computing Science>Decision and Computing Science</option>
</select>
<select class="form-control preference-select"  name="preference2">
  <option value=""></option>
</select>
<select class="form-control preference-select"  name="preference3" >
<option value=""></option>
</select>
<select class="form-control preference-select"  name="preference4">
<option value=""></option>
</select></div>`
}

}
document.addEventListener("DOMContentLoaded", function () {
  const autosavedFormData =
    JSON.parse(localStorage.getItem("autosavedFormData")) || {};
    addSubjectRows("science");

  for (const key in autosavedFormData) {
    if (Object.hasOwnProperty.call(autosavedFormData, key)) {
      const value = autosavedFormData[key];
      const inputElement = document.querySelector(`[name="${key}"]`);
      if (inputElement) {
        inputElement.value = value;
      }
    }
  }
});
var radioBtn1 = document.getElementById("scienceRadio");
    radioBtn1.addEventListener("change", function() {
        if (radioBtn1.checked) {
            addSubjectRows("science");
        }
    });
var radioBtn2 = document.getElementById("commerceRadio");
    radioBtn2.addEventListener("change", function() {
        if (radioBtn2.checked) {
            addSubjectRows("commerce");
        }
    });
const inputElements = document.querySelectorAll("input, select, textarea");
inputElements.forEach(function (input) {
  input.addEventListener("input", function () {
    const formData = {};
    inputElements.forEach(function (input) {
      formData[input.name] = input.value;
    });
    localStorage.setItem("autosavedFormData", JSON.stringify(formData));
  });
});



$(function () {
  $(document).on("change", "select", function () {
    var used = new Set();
    $("select").each(function () {
      var reset = false;
      $("option", this).each(function () {
        if ($(this).text() === "Select Subject") return;
        var hide = used.has($(this).text());
        if (hide && $(this).is(":selected")) {
          reset = true;
        }
        $(this).prop("hidden", hide);
      });
      if (reset) {
        $("option:not([hidden]):first", this).prop("selected", true);
      }
      used.add($("option:selected", this).text());
    });
  });
});


function calculateAge() {
  var dobInput = document.getElementById("dob").value;
  var dob = new Date(dobInput);
  var today = new Date();

  var age = today.getFullYear() - dob.getFullYear();
  var monthDiff = today.getMonth() - dob.getMonth();
  if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < dob.getDate())) {
      age--;
  }

  document.getElementById("age").value = age;
}