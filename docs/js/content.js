var CONTENT = [
    {
        img: "about.jpg",
        id: "about",
        title: "About",
        content: "Hey there, I'm Naveen. I'm currently a junior at <a href = 'https://mbhs.edu'>Montgomery Blair HS</a>.<br/><br/>\
                    Stuff I like:\
                    <br/><ul><li>Research</li><li>Hackathons</li><li>Tennis</li><li>Piano</li></ul>\
                    Stuff I dislike:\
                    <br/><ul><li>Game controllers with convex sticks (why?)</li><li>Apple products</li><li>Shoelaces</li></ul>\
                    Here's my <a href = 'http://github.com/ndurvasula'>GitHub</a>, <a href = 'https://devpost.com/CodeIntegrity'>Devpost</a>, and <a href = 'cv.pdf'>CV</a>."
    },
    {
        img: "mlh.jpg",
        id: "hacks",
        title: "A Test",
        content: "Here's a running list of hackathon projects:" +
        		"<ul><li><a href = 'https://devpost.com/software/cadvr'>CADVR</a> - a VR CAD viewer - HackUMBC Spring 2016 - Winner -  Best Tool for Developers </li>" +
        		"<li><a href = 'https://devpost.com/software/vrmc'>IMUCAP</a> - an affordable VR motion capture system for gaming - HackUMBC Fall 2016 - Winner - Most Innovative Game</li>" +
        		"<li><a href = 'https://devpost.com/software/fridgesight'>FridgeSight</a> - converts any fridge into an affordable smart fridge - PennApps XVI - Winner - Hasura Special Prize</li></ul>"
    },
    {
        img: "muff.jpg",
        id: "muff",
        title: "Testing",
        content: "<p>The muffin problem is a simple problem to understand, and fun to solve too.</p>" +
        		"<p>We are given <i>m</i> muffins and <i>s</i> students, and everyone wants " +
        		"<i>m/s</i> muffins. Take, for example, 5 muffins (1-5) and 3 students (A, B, C). As everyone needs " +
        		"5/3 of a muffin, a possible protocol could be each person 1 muffin, and then take the two remaining " +
        		"muffins and split them into 1/3 and 2/3. We can give A and B each a 2/3 sized piece, and give the remaining " +
        		"2 1/3 sized pieces to C. However, this makes C mad, as C gets a small piece. What protocol provably maximizes " +
        		"the size of the smallest piece? More generally, what is the size of the smallest piece for all <i>m</i> and <i>s</i>?" +
        		"</p><p>The full paper is on <a href = 'https://arxiv.org/abs/1709.02452'>arXiv</a>. " +
        		"This work is an invited presentation at the " +
        		"<a href = 'http://jointmathematicsmeetings.org/jmm'>Joint Mathematics Meeting of the AMS and MAA</a>. and will be submitted to " +
                        "<a href = 'https://sites.google.com/view/fun2018/'>FUN 2018</a>"
    },
    {
        img: "isef.jpg",
        id: "kidneys",
        title: "Quality Assurance",
        content: "<p>I <a href = 'http://github.com/ndurvasula/KPDMetric'></a> developed a participant-specific estimate of expected organ quality in a kidney paired donation system.\
                    Essentially, if you are a patient with end-stage renal disease, and wish to enter a kidney paired donation system (a system in which\
                    patients paired with incompatible donors trade with other such pairs to receive a kidney), my work aims to tell you what the quality of the kidney you will receive is,\
                    as well as how long it will take for you to receive this kidney. </p>\
                    <p>This work was done under the guidance of <a href = 'http://jpdickerson.com/'>Assistant Prof. John Dickerson</a> and <a href = 'https://www.cs.umd.edu/~srin/'>Prof. Aravind Srinivasan</a>\
                    from the University of Maryland. I got a mention <a href = 'https://www.cs.umd.edu/article/2017/03/professor-aravind-srinivasan-and-assistant-professor-john-dickerson-mentor-award'>here</a>\
                    for being an <a href = 'https://student.societyforscience.org/intel-isef'>Intel ISEF finalist</a>. The simulator that I made as part of this project was used in <a href = 'https://users.cs.duke.edu/~conitzer/kidneyAAAI18.pdf'>this</a> paper \
                    which was accepted the <a href = 'http://aaai.org/Conferences/AAAI/aaai18.php'>AAAI 18</a> conference. This work \
                    will be submitted to the <a href = 'http://auai.org/uai2018/index.php'>UAI</a> conference, and eventually the <a href = 'http://onlinelibrary.wiley.com/journal/10.1111/(ISSN)1600-6143'>American Journal of Transplantation</a>. \
                    At ISEF, this project won the <a href = 'http://www.avasc.com/'>AVASC</a> award.</p>"
    },
    {
    	img: "bgb.jpg",
    	id: "systems",
    	title: "MBHS Systems",
    	content: "<p><a href = 'http://mbhs.systems'>MBHS Systems</a> is a club that I am starting, that aims to bring some entrepreneurial and group based research to Montgomery Blair HS. " +
		"As a program that claims that it is based around research, <a href = 'https://mbhs.edu/departments/magnet/'>Montgomery Blair HS Magnet</a> really only has the Senior Research Project to show for it. The objective of MBHS systems " +
		"is to demonstrate how impactful MBHS students can be. The club centers around the idea, design, development, and deployment of a product. The problem to be solved is " +
		"very technically challenging, spanning several fields in STEM, and MBHS Systems aims to solve and deploy a solution over the couse of a year.</p>" +
		"<p>This year, MBHS Systems will solve the problem of global pollen modelling using satellite imagery. From satellite imagery of a region, features such as " +
		"what trees are there, what the terrain is, and what bodies of water are there will be extracted. Using that in conjunction with how current weather systems are " +
		"behaving in the region allows for the prediction for the concentration of pollen in the area. The concentration will be converted into a readable value for the user. " +
		"Users can also select what species of trees they are allergic to, and from that, they can get a personalized value. The app will also learn from the subjective input of " +
		"the user to give the user a personalized value for the metric.</p>"
    }

]
function addContent(img, title, content, id, start) {
    var post = document.createElement("section");
    post.id = id;
    
    var cont = document.createElement("div");
    cont.className = "container post";
    cont.dataset.bg = img;
    
    var im = document.createElement("img");
    im.id = img;
    im.src = "img/"+img;
    if (start)
        im.className = "opaque";

    document.getElementById("con").appendChild(im);

    var row = document.createElement("div");
    row.className = "row";
    

    var t1 = document.createElement("div");
    t1.className = "col-lg-12";

    var t2 = document.createElement("div");
    t2.className = "section-title";

    var h = document.createElement("h1");
    h.innerHTML = title;

    var p = document.createElement("div");
    p.className = "cbody";
    p.innerHTML = content;

    t2.appendChild(h);
    t1.appendChild(t2);
    row.appendChild(t1);
    row.appendChild(p);
    cont.appendChild(row);
    post.appendChild(cont);
    document.getElementById('page-top').appendChild(post);

}
for (var i = 0; i < CONTENT.length; i++) {
    start = i == 0;

    //update navbar
    var ln = document.createElement("li");

    var an = document.createElement("a");
    an.href = "#" + CONTENT[i].id;
    an.className = "page-scroll";
    an.innerHTML = CONTENT[i].title;

    ln.appendChild(an);
    document.getElementById('link').appendChild(ln);

    //add content
    addContent(CONTENT[i].img, CONTENT[i].title, CONTENT[i].content, CONTENT[i].id, start);
}
