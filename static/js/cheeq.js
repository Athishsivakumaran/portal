const text =
  "We are delighted to have you here as you embark on your journey towards advanced learning and academic excellence. Explore our offerings, discover your potential, and take the first step towards a rewarding future with CIT. We wish you the best of luck in your pursuit of higher education.";
let index = 0;

function typeWriter() {
  if (index < text.length) {
    document.getElementById("typing-text1").innerHTML += text.charAt(index);
    index++;
    setTimeout(typeWriter, 10);
  }
}

typeWriter();

function submitForm() {
  var form = document.getElementById("marks");
  var formData = new FormData(form);
  fetch("/", {
    method: "POST",
    body: formData,
  }).then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  });
}

function refresh() {
  var elg = document.getElementById("eligibility");
  var eligib = document.getElementById("eligib");
  elg.innerText = "";
  eligib.value = "No";
}

function checkRange(input) {
  var total = document.getElementById((parseInt(input.id) + 1).toString());
  if (input.value < 1 || input.value > parseInt(total.value)) {
    input.value = "";
  }
  refresh();
}

function eligible(status) {
  var elg = document.getElementById("eligibility");
  var eligib = document.getElementById("eligib");
  if (status == true) {
    elg.innerText = "You are eligible to apply .";
    eligib.value = "Yes";
  } else {
    /*
    elg.innerHTML =
      '<div class="loading-dots"><span class="loading-dot"></span><span class="loading-dot"></span><span class="loading-dot"></span></div>';
    var reason = "";
    var formData = new FormData(document.getElementById("marks"));
    fetch("/eligibility_api", {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        var loadingAnimation = document.querySelector(".loading-dots");
        loadingAnimation.parentNode.removeChild(loadingAnimation);
        reason = data.data;
        elg.innerText = "You are not eligible to apply . " + reason;
        eligib.value = "No";
      })
      .catch((error) => {
        console.error("There was a problem with the fetch operation:", error);
        var loadingAnimation = document.querySelector(".loading-dots");
        loadingAnimation.parentNode.removeChild(loadingAnimation);

        elg.innerText = "Error fetching data";
      });*/
    elg.innerHTML =
      "You are not eligible to apply. You need to have an aggregate of 75% and above in Mathematics, Physics, and Chemistry or Computer Science";
    eligib.value = "No";
  }

  submitForm();
}

function checkValues(event) {
  event.preventDefault();
  for (var i = 0; i <= 12; i++) {
    if (document.getElementById(i.toString()).value == "") {
      refresh();
      var elg = document.getElementById("eligibility");
      elg.innerText = "Please enter the required details in order to proceed!";
      return;
    }
  }
  var numbers = [];
  for (var i = 0; i < 15; i = i + 3) {
    var num =
      parseInt(document.getElementById((i + 2).toString()).value) /
      parseInt(document.getElementById((i + 3).toString()).value);
    if (num < 0.5) {
      eligible(false);
      return;
    }
    numbers.push(num);
  }
  var status = document.getElementById("status");
  if (document.getElementById("10".toString()).value == "Computer Science") {
    if (status.value == "Science") {
      numbers[2] = Math.max(numbers[2], numbers[3]);
    } else {
      let num1 = Math.max(numbers[1], numbers[2], numbers[3]);
      let num2 = [numbers[1], numbers[2], numbers[3]].sort()[1];
      numbers[1] = num1;
      numbers[2] = num2;
    }
  }
  var total = 0;
  for (var i = 0; i < 3; i++) {
    var total = total + numbers[i];
  }
  if (total / 3 < 0.75) {
    eligible(false);
  } else {
    eligible(true);
  }
}

function toggleColor(stream) {
  var pills = document.querySelectorAll(".pill");
  var scienceCourses = document.getElementById("scienceCourses");
  var artsCourses = document.getElementById("artsCourses");
  var status = document.getElementById("status");
  if (stream === "Arts") {
    status.value = "Arts";
    scienceCourses.style.display = "none";
    artsCourses.style.display = "block";
    pills[0].classList.add("white");
    pills[0].classList.remove("black");
    pills[1].classList.add("black");
    pills[1].classList.remove("white");
    var subjectOptions = [
      '<select id="1" name="first_subject" class="form-contrl" oninput="refresh()" required><option value="" selected disabled>Select Subject</option> <option value="Mathematics">Mathematics</option><option value="Statistics">Statistics</option><option value="Business Mathematics">Business Mathematics</option><option value="Applied Mathematics">Applied Mathematics</option><option value="Business Mathematics and Statistics">Business Mathematics and Statistics</option></select>',
      '<select id="4" name="second_subject" class="form-contrl" oninput="refresh()" required><option value="" selected disabled>Select Subject</option> <option value="Commerce">Commerce</option><option value="Economics">Economics</option><option value="Accountancy">Accountancy</option></select>',
      '<select id="7" name="third_subject" class="form-contrl" oninput="refresh()" required><option value="" selected disabled>Select Subject</option> <option value="Commerce">Commerce</option><option value="Economics">Economics</option><option value="Accountancy">Accountancy</option></select>',
      '<select id="10" name="fourth_subject" class="form-contrl" oninput="refresh()" required><option value="" selected disabled>Select Subject</option> <option value="Computer Science">Computer Science</option><option value="Information Practices">Information Practices</option></select>',
    ];
    refresh();
  } else {
    status.value = "Science";
    scienceCourses.style.display = "block";
    artsCourses.style.display = "none";
    pills[0].classList.add("black");
    pills[0].classList.remove("white");
    pills[1].classList.add("white");
    pills[1].classList.remove("black");
    var subjectOptions = [
      '<input id="1" name="first_subject" type="text" class="form-contrl" value="Maths" readonly />',
      '<input id="4" class="form-contrl" type="text" name="second_subject" value="Physics" readonly />',
      '<input id="7" class="form-contrl" type="text" name="third_subject" value="Chemistry" readonly />',
      '<select id="10" name="fourth_subject" class="form-contrl" oninput="refresh()" required><option value="" selected disabled>Select Subject</option> <option value="Computer Science">Computer Science</option><option value="Information Practices">Information Practices</option><option value="Biology">Biology</option></select>',
    ];
  }

  for (var i = 0; i < subjectOptions.length; i++) {
    var parentElement = document.getElementById((i + 13).toString());
    parentElement.innerHTML = subjectOptions[i];
  }

  refresh();
}

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
