const body = document.querySelector("body"),
      sidebar = body.querySelector(".sidebar"),
      sidebar2 = body.querySelector(".sidebar2"), 
      menu = body.querySelector(".sidebar2"),   
      toggle = body.querySelector(".toggle"),
      modeSwitch = body.querySelector(".toggle-switch"),
      modeText = body.querySelector(".mode-text");  


      toggle.addEventListener("click", ()=>{
        sidebar.classList.toggle("close");
      });


      modeSwitch.addEventListener("desativado", ()=>{
        body.classList.toggle("dark");

        if(body.classList.contains("dark")){
            modeText.innerText = "Dark Mode"
        }else{
            modeText.innerText = "Light Mode"
        }
      });


const selected = document.querySelector(".selected");
const optionsContainer = document.querySelector(".options-container");

const optionsList = document.querySelectorAll(".option");

selected.addEventListener("click", ()=>{
    optionsContainer.classList.toggle("active");
});

optionsList.forEach( o => {
    o.addEventListener("click", () =>{
        selected.innerHTML = o.querySelector("label").innerHTML;
        optionsContainer.classList.remove("active");
    });
});

const navv = document.querySelector(".navv"),
      navvList = navv.querySelectorAll("li"),
      totalNavvList = navvList.length;

      for (let i=0; i<totalNavvList; i++)
      {
        const a = navvList[i].querySelector("a");
        a.addEventListener("click", function()
        {
            for (let j=0; j<totalNavvList; j++)
            {
                navvList[j].querySelector("a").classList.remove("active");
            }
            this.classList.add("active")
        })
      }