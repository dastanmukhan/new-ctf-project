from flask import Flask, render_template_string, request

app = Flask(__name__)

# Логин и пароль
login = "admin123"
password = "СTFLABS2025"

@app.route("/")
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login Page</title>
    </head>
    <body>
        <h1>Welcome to the CTF Challenge!</h1>
        <p>Find the login and password .</p>
        
        <h2>Login Form:</h2>
        <form action="/verify" method="POST">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br><br>
            
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br><br>
            
            <input type="submit" value="Login">
        </form>
        
        <p></p>
        <p><a href="/code">Click here to see the code</a></p>
    </body>
    </html> 
                                  
    """)

@app.route("/code")
def code_page():
    return render_template_string("""
    <<html lang="en">
                                  
  <body monica-id="ofpnmcalabcbjgholdjcjblkibolbppb" monica-version="7.6.0"><div role="dialog" aria-live="polite" aria-label="cookieconsent" aria-describedby="cookieconsent:desc" class="cc-window cc-floating cc-type-info cc-theme-block cc-bottom cc-right cc-color-override--1057083089 " style=""><!--googleoff: all--><span id="cookieconsent:desc" class="cc-message">This website uses cookies to manage authentication, for analytics, and other functions. <a aria-label="learn more about cookies" role="button" tabindex="0" class="cc-link" href="https://ctftime.org/privacy" rel="noopener noreferrer nofollow" target="_blank"></a></span><div class="cc-compliance"><a aria-label="dismiss cookie message" role="button" tabindex="0" class="cc-btn cc-dismiss">Got it!</a></div><!--googleon: all--></div>

    <div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <a class="brand" href="//ctftime.org/"><img src="/static/images/ct/logo.svg" alt="CTFtime.org" border="0" width="191px"></a>
          <div class="nav-collapse">
            <ul class="nav">
              <li><a href="/ctfs">CTFs</a></li>
              <li><a href="/event/list/upcoming">Upcoming</a></li>
              <li class="dropdown">
                 <a href="#" class="dropdown-toggle" data-toggle="dropdown">Archive  <b class="caret"></b></a>
                  <ul class="dropdown-menu">
                  <li><a href="/event/list/past">Past events</a></li>
                  <li><a href="/tasks/">Tasks</a></li>
                  <li><a href="/writeups">Writeups</a></li>
                  </ul>
              </li>
              <li><a href="/calendar/">Calendar</a></li>
              <li class="dropdown">
                 <a href="#" class="dropdown-toggle" data-toggle="dropdown">Teams  <b class="caret"></b></a>
                  <ul class="dropdown-menu">
                  <li><a href="/stats/">Rating</a></li>
                  <li><a href="/team/compare">Compare</a></li>
                  <li><a href="/team/new/">Create new team</a></li>
                  <li><a href="/dating">Get team members</a></li>
                  </ul>
              </li>
              <li><a href="/faq/">FAQ</a></li>
              <li class="dropdown">
                 <a href="#" class="dropdown-toggle" data-toggle="dropdown">Contact us  <b class="caret"></b></a>
                  <ul class="dropdown-menu">
                  <li><a href="/event/mail">For organizers</a></li>
                  <li><a href="/feedback">Feedback</a></li>
                  </ul>
              </li>
              <li><a href="/about/">About</a></li>
            </ul>
            <ul class="nav pull-right">
            
            <li><a href="/profile">Timezone: UTC</a></li>
            
            <li class="divider-vertical"></li>
                
                <li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown"><!-- Welcome, -->mukandastan <b class="caret"></b></a>
                  <ul class="dropdown-menu">
                    <li><a href="/profile">Profile</a></li>
                    
                    <li class="divider"></li>
                    <li><a href="/logout/">Sign out</a></li>
                  </ul>
                </li>
                
            </ul>
          </div>
        </div>
      </div>
    </div>


    

<ul class="breadcrumb">
    <li><a href="/">Home</a> <span class="divider">/</span></li>

    <li class="active">Teams</li>

</ul>


    <div class="container">

    

    


<div class="page-header">
<h2>Teams</h2>
</div>

<ul class="nav nav-pills">
    
        
        <li><a href="/stats/2023">2023</a></li>
        <li><a href="/stats/2022">2022</a></li>

        <li><a href="/stats/2021">2021</a></li>
        <li><a href="/stats/2020">2020</a></li>
        <li><a href="/stats/2019">2019</a></li>
        <li><a href="/stats/2018">2018</a></li>
        <li><a href="/stats/2017">2017</a></li>
        <li><a href="/stats/2016">2016</a></li>
        <li><a href="/stats/2015">2015</a></li>
        <li><a href="/stats/2014">2014</a></li>
        <li><a href="/stats/2013">2013</a></li>
        <li><a href="/stats/2012">2012</a></li>
        <li><a href="/stats/2011">2011</a></li>
        
        <li><a href="/stats/ac/2024">Academic</a></li>
        
        <li class="dropdown">
        <a class="dropdown-toggle" data-toggle="dropdown" href="#">Country <b class="caret"></b></a>
        <ul class="dropdown-menu">
        <li><a href="/stats/2024">---</a></li>    
        
        <li><a href="/stats/2024/AF">Афганистан</a></li>
        
        <li><a href="/stats/2024/AX">Аландские острова</a></li>
        
        <li><a href="/stats/2024/AL">Албания</a></li>
        
        <li><a href="/stats/2024/DZ">Алжир</a></li>
        
        <li><a href="/stats/2024/AS">Американское Самоа</a></li>
        
        <li><a href="/stats/2024/AD">Андорра</a></li>
        
        <li><a href="/stats/2024/AO">Ангола</a></li>
        
        <li><a href="/stats/2024/AI">Ангилья</a></li>
        
        <li><a href="/stats/2024/AQ">Антарктида</a></li>
        
        <li><a href="/stats/2024/AG">Антигуа и Барбуда</a></li>
        
        <li><a href="/stats/2024/AR">Аргентина</a></li>
        
        <li><a href="/stats/2024/AM">Армения</a></li>
        
        <li><a href="/stats/2024/AW">Аруба</a></li>
        
        <li><a href="/stats/2024/AU">Австралия</a></li>
        
        <li><a href="/stats/2024/AT">Австрия</a></li>
        
        <li><a href="/stats/2024/AZ">Азербайджан</a></li>
        
        <li><a href="/stats/2024/BS">Багамские острова</a></li>
        
        <li><a href="/stats/2024/BH">Бахрейн</a></li>
        
        <li><a href="/stats/2024/BD">Бангладеш</a></li>
        
        <li><a href="/stats/2024/BB">Барбадос</a></li>
        
        <li><a href="/stats/2024/BY">Беларусь</a></li>
        
        <li><a href="/stats/2024/BE">Бельгия</a></li>
        
        <li><a href="/stats/2024/BZ">Белиз</a></li>
        
        <li><a href="/stats/2024/BJ">Бенин</a></li>
        
        <li><a href="/stats/2024/BM">Бермудские острова</a></li>
        
        <li><a href="/stats/2024/BT">Бутан</a></li>
        
        <li><a href="/stats/2024/BO">БУтан</a></li>
        
        <li><a href="/stats/2024/BQ">Bonaire, Sint Eustatius and Saba</a></li>
        
        <li><a href="/stats/2024/BA">Босния и Герцеговина</a></li>
        
        <li><a href="/stats/2024/BW">Ботсвана</a></li>
        
        <li><a href="/stats/2024/BV">Остров Буве</a></li>
        
        <li><a href="/stats/2024/BR">Бразилия</a></li>
        
        <li><a href="/stats/2024/IO">Британская территория в Индийском океане</a></li>
        
        <li><a href="/stats/2024/BN">Бруней-Даруссалам</a></li>
        
        <li><a href="/stats/2024/BG">Болгария</a></li>
        
        <li><a href="/stats/2024/BF">Буркина-Фасо</a></li>
        
        <li><a href="/stats/2024/BI">Бурунди</a></li>
        
        <li><a href="/stats/2024/KH">Камбоджа</a></li>
        
        <li><a href="/stats/2024/CM">Камерун</a></li>
        
        <li><a href="/stats/2024/CA">Канада</a></li>
        
        <li><a href="/stats/2024/CV">Кабо-Верде</a></li>
        
        <li><a href="/stats/2024/KY">Каймановы острова</a></li>
        
        <li><a href="/stats/2024/CF">Центральноафриканская Республика</a></li>
        
        <li><a href="/stats/2024/TD">Чад</a></li>
        
        <li><a href="/stats/2024/CL">Чили</a></li>
        
        <li><a href="/stats/2024/CN">Китай</a></li>
        
        <li><a href="/stats/2024/CX">Остров Рождества</a></li>
        
        <li><a href="/stats/2024/CC">Кокосовые (Килинг) острова</a></li>
        
        <li><a href="/stats/2024/CO">Колумбия</a></li>
        
        <li><a href="/stats/2024/KM">Коморские острова</a></li>
        
        <li><a href="/stats/2024/CG">Конго</a></li>
        
        <li><a href="/stats/2024/CD">Конго, Демократическая Республика</a></li>
        
        <li><a href="/stats/2024/CK">Острова Кука</a></li>
        
        <li><a href="/stats/2024/CR">Коста-Рика</a></li>
        
        <li><a href="/stats/2024/CI">Кот-д'Ивуар</a></li>
        
        <li><a href="/stats/2024/HR">Хорватия</a></li>
        
        <li><a href="/stats/2024/CU">Куба</a></li>
        
        <li><a href="/stats/2024/CW">Кюрасао</a></li>
        
        <li><a href="/stats/2024/CY">Кипр</a></li>
        
        <li><a href="/stats/2024/CZ">Чешская Республика</a></li>
        
        <li><a href="/stats/2024/DK">Дания</a></li>
        
        <li><a href="/stats/2024/DJ">Джибути</a></li>
        
        <li><a href="/stats/2024/DM">Доминика</a></li>
        
        <li><a href="/stats/2024/DO">Доминиканская Республика</a></li>
        
        <li><a href="/stats/2024/EC">Эквадор</a></li>
        
        <li><a href="/stats/2024/EG">Египет</a></li>
        
        <li><a href="/stats/2024/SV">Сальвадор</a></li>
        
        <li><a href="/stats/2024/GQ">Экваториальная Гвинея</a></li>
        
        <li><a href="/stats/2024/ER">Эритрея</a></li>
        
        <li><a href="/stats/2024/EE">Эстония</a></li>
        
        <li><a href="/stats/2024/ET">Эфиопия</a></li>
        
        <li><a href="/stats/2024/FO">Фарерские острова</a></li>
        
        <li><a href="/stats/2024/FJ">Фиджи</a></li>
        
        <li><a href="/stats/2024/FI">Финляндия</a></li>
        
        <li><a href="/stats/2024/FR">Франция</a></li>
        
        <li><a href="/stats/2024/GF">Французская Гвиана</a></li>
        
        <li><a href="/stats/2024/PF">Французская Полинезия</a></li>
        
        <li><a href="/stats/2024/TF">Французские южные территории</a></li>
        
        <li><a href="/stats/2024/GA">Габон</a></li>
        
        <li><a href="/stats/2024/GM">Гамбия</a></li>
        
        <li><a href="/stats/2024/GE">Грузии</a></li>
        
        <li><a href="/stats/2024/DE">Германия</a></li>
        
        <li><a href="/stats/2024/GH">Гана</a></li>
        
        <li><a href="/stats/2024/GI">Гибралтар</a></li>
        
        <li><a href="/stats/2024/GR">Греция</a></li>
        
        <li><a href="/stats/2024/GL">Гренландия</a></li>
        
        <li><a href="/stats/2024/GD">Гренада</a></li>
        
        <li><a href="/stats/2024/GU">Гуам</a></li>
        
        <li><a href="/stats/2024/GT">Гватемала</a></li>
        
        <li><a href="/stats/2024/GG">Гернси</a></li>
        
        <li><a href="/stats/2024/GN">Гвинея</a></li>
        
        <li><a href="/stats/2024/HT">Гаити</a></li>
        
        <li><a href="/stats/2024/HM">Остров Херд и Острова Макдоналд</a></li>
        
        <li><a href="/stats/2024/VA">Святейший Престол (Государство Ватикан"admin")</a></li>
        
        <li><a href="/stats/2024/HN">l:</a></li>
        
        <li><a href="/stats/2024/HK">Гонконг</a></li>
        
        <li><a href="/stats/2024/HU">Венгрия"123"</a></li>
        
        <li><a href="/stats/2024/IS">Исландия</a></li>
        
        <li><a href="/stats/2024/IN">Индия</a></li>
        
        <li><a href="/stats/2024/ID">Индонезия</a></li>
        
        <li><a href="/stats/2024/IR">Иран, Исламская Республика</a></li>
        
        <li><a href="/stats/2024/IQ">Ирак</a></li>
        
        <li><a href="/stats/2024/IE">Ирландия</a></li>
        
        <li><a href="/stats/2024/IM">Остров Мэн</a></li>
        
        <li><a href="/stats/2024/IL">Израиль</a></li>
        
        <li><a href="/stats/2024/IT">Италия</a></li>
        
        <li><a href="/stats/2024/JM">Ямайка</a></li>
        
        <li><a href="/stats/2024/JP">Япония</a></li>
        
        <li><a href="/stats/2024/JO">Иордания</a></li>
        
        <li><a href="/stats/2024/KZ">Казахстан</a></li>
        
        <li><a href="/stats/2024/KE">Кения</a></li>
        
        <li><a href="/stats/2024/KI">Кирибати</a></li>
        
        <li><a href="/stats/2024/KP">Корея, Народно-Демократическая Республика</a></li>
        
        <li><a href="/stats/2024/KR">Корея, Республика</a></li>
        
        
        
        </ul>
        </li>
        
    
</ul>

<div class="well">
    <form class="form-search" method="post" action="/team/list/"><div style="display:none"><input type="hidden" name="csrfmiddlewaretoken" value="kCGV4rFbJHAuZApUyGygreiFmBiAsgbZ"></div>
        <span class="twitter-typeahead" style="position: relative; display: inline-block;"><input class="tt-hint" type="text" autocomplete="off" spellcheck="off" disabled="" style="position: absolute; top: 0px; left: 0px; border-color: transparent; box-shadow: none; background: none 0% 0% / auto repeat scroll padding-box border-box rgb(255, 255, 255);"><input type="text" name="team_name" data-provide="typeahead" class="typeahead tt-query" autocomplete="off" spellcheck="false" dir="auto" style="position: relative; vertical-align: top; background-color: transparent;"><span style="position: absolute; left: -9999px; visibility: hidden; white-space: nowrap; font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size: 13px; font-style: normal; font-variant: normal; font-weight: 400; word-spacing: 0px; letter-spacing: 0px; text-indent: 0px; text-rendering: auto; text-transform: none;"></span><span class="tt-dropdown-menu" style="position: absolute; top: 100%; left: 0px; z-index: 100; display: none;"></span></span>
        <button type="submit" class="btn btn-primary btn-search">Show team profile</button>
    </form>
</div>


    <table class="table table-striped">
    <tbody><tr><th colspan="2">Worldwide position</th><th>Name</th><th>Country</th><th>Points</th><th>Events</th></tr>
    
        <tr><td class="place leader">1</td><td></td><td><a href="/team/114856">kalmarunionen</a></td><td class="country"><a href="/stats/2024/DK"><img src="/static/images/sf/dk.svg" alt="DK"></a></td><td>1721,038</td><td>49</td></tr>
    
        <tr><td class="place">2</td><td></td><td><a href="/team/220769">Friendly Maltese Citizens</a></td><td class="country"><a href="/stats/2024/MT"><img src="/static/images/sf/mt.svg" alt="MT"></a></td><td>1175,626</td><td>16</td></tr>
    
        <tr><td class="place">3</td><td></td><td><a href="/team/85618">thehackerscrew</a></td><td class="country"><a href="/stats/2024/AQ"><img src="/static/images/sf/aq.svg" alt="AQ"></a></td><td>1131,854</td><td>60</td></tr>
    
        <tr><td class="place">4</td><td></td><td><a href="/team/83435">C4T BuT S4D</a></td><td class="country"><a href="/stats/2024/RU"><img src="/static/images/sf/ru.svg" alt="RU"></a></td><td>1102,239</td><td>16</td></tr>
    
        <tr><td class="place">5</td><td></td><td><a href="/team/58979">r3kapig</a></td><td class="country"><a href="/stats/2024/CN"><img src="/static/images/sf/cn.svg" alt="CN"></a></td><td>1038,701</td><td>74</td></tr>
    
        <tr><td class="place">6</td><td></td><td><a href="/team/205897">💦​</a></td><td class="country"></td><td>966,621</td><td>19</td></tr>
    
        <tr><td class="place">7</td><td></td><td><a href="/team/87434">The Flat Network Society</a></td><td class="country"><a href="/stats/2024/FR"><img src="/static/images/sf/fr.svg" alt="FR"></a></td><td>917,042</td><td>58</td></tr>
    
        <tr><td class="place">8</td><td></td><td><a href="/team/13575">Never Stop Exploiting</a></td><td class="country"><a href="/stats/2024/CN"><img src="/static/images/sf/cn.svg" alt="CN"></a></td><td>898,382</td><td>14</td></tr>
    
        <tr><td class="place">9</td><td></td><td><a href="/team/42934">organizers</a></td><td class="country"><a href="/stats/2024/CH"><img src="/static/images/sf/ch.svg" alt="CH"></a></td><td>867,255</td><td>35</td></tr>
    
        <tr><td class="place">10</td><td></td><td><a href="/team/169557">Project Sekai</a></td><td class="country"></td><td>838,668</td><td>23</td></tr>
    
        <tr><td class="place">11</td><td></td><td><a href="/team/551">FluxFingers</a></td><td class="country"><a href="/stats/2024/DE"><img src="/static/images/sf/de.svg" alt="DE"></a></td><td>817,058</td><td>27</td></tr>
    
        <tr><td class="place">12</td><td></td><td><a href="/team/33893">justCatTheFish</a></td><td class="country"><a href="/stats/2024/PL"><img src="/static/images/sf/pl.svg" alt="PL"></a></td><td>778,705</td><td>26</td></tr>
    
        <tr><td class="place">13</td><td></td><td><a href="/team/222911">.;,;.</a></td><td class="country"><a href="/stats/2024/US"><img src="/static/images/sf/us.svg" alt="US"></a></td><td>738,672</td><td>27</td></tr>
    
        <tr><td class="place">14</td><td></td><td><a href="/team/586">Bushwhackers</a></td><td class="country"><a href="/stats/2024/RU"><img src="/static/images/sf/ru.svg" alt="RU"></a></td><td>732,760</td><td>22</td></tr>
    
        <tr><td class="place">15</td><td></td><td><a href="/team/109452">DiceGang</a></td><td class="country"><a href="/stats/2024/US"><img src="/static/images/sf/us.svg" alt="US"></a></td><td>721,175</td><td>14</td></tr>
    
        <tr><td class="place">16</td><td></td><td><a href="/team/211952">SKSD</a></td><td class="country"><a href="/stats/2024/ID"><img src="/static/images/sf/id.svg" alt="ID"></a></td><td>696,950</td><td>27</td></tr>
    
        <tr><td class="place">17</td><td></td><td><a href="/team/157039">idek</a></td><td class="country"></td><td>694,079</td><td>38</td></tr>
    
        <tr><td class="place">18</td><td></td><td><a href="/team/193832">TeamItaly</a></td><td class="country"><a href="/stats/2024/IT"><img src="/static/images/sf/it.svg" alt="IT"></a></td><td>684,462</td><td>11</td></tr>
    
        <tr><td class="place">19</td><td></td><td><a href="/team/1438">ENOFLAG</a></td><td class="country"><a href="/stats/2024/DE"><img src="/static/images/sf/de.svg" alt="DE"></a></td><td>667,882</td><td>23</td></tr>
    
        <tr><td class="place">20</td><td></td><td><a href="/team/19208">Nu1L</a></td><td class="country"><a href="/stats/2024/CN"><img src="/static/images/sf/cn.svg" alt="CN"></a></td><td>661,397</td><td>20</td></tr>
    
        <tr><td class="place">21</td><td></td><td><a href="/team/220336">L3ak</a></td><td class="country"></td><td>643,005</td><td>43</td></tr>
    
        <tr><td class="place">22</td><td></td><td><a href="/team/662">bi0s</a></td><td class="country"><a href="/stats/2024/IN"><img src="/static/images/sf/in.svg" alt="IN"></a></td><td>593,836</td><td>69</td></tr>
    
        <tr><td class="place">23</td><td></td><td><a href="/team/269765">BunkyoWesterns</a></td><td class="country"><a href="/stats/2024/JP"><img src="/static/images/sf/jp.svg" alt="JP"></a></td><td>584,111</td><td>33</td></tr>
    
        <tr><td class="place">24</td><td></td><td><a href="/team/4140">ASIS</a></td><td class="country"><a href="/stats/2024/IR"><img src="/static/images/sf/ir.svg" alt="IR"></a></td><td>570,393</td><td>11</td></tr>
    
        <tr><td class="place">25</td><td></td><td><a href="/team/60467">pwnthem0le</a></td><td class="country"><a href="/stats/2024/IT"><img src="/static/images/sf/it.svg" alt="IT"></a></td><td>567,253</td><td>14</td></tr>
    
        <tr><td class="place">26</td><td></td><td><a href="/team/224122">ierae</a></td><td class="country"><a href="/stats/2024/JP"><img src="/static/images/sf/jp.svg" alt="JP"></a></td><td>564,187</td><td>12</td></tr>
    
        <tr><td class="place">27</td><td></td><td><a href="/team/73723">Maple Bacon</a></td><td class="country"><a href="/stats/2024/CA"><img src="/static/images/sf/ca.svg" alt="CA"></a></td><td>555,140</td><td>57</td></tr>
    
        <tr><td class="place">28</td><td></td><td><a href="/team/157017">dtl</a></td><td class="country"><a href="/stats/2024/RU"><img src="/static/images/sf/ru.svg" alt="RU"></a></td><td>551,853</td><td>19</td></tr>
    
        <tr><td class="place">29</td><td></td><td><a href="/team/139261">UofTCTF</a></td><td class="country"><a href="/stats/2024/CA"><img src="/static/images/sf/ca.svg" alt="CA"></a></td><td>550,562</td><td>45</td></tr>
    
        <tr><td class="place">30</td><td></td><td><a href="/team/274071">Superflat</a></td><td class="country"><a href="/stats/2024/NL"><img src="/static/images/sf/nl.svg" alt="NL"></a></td><td>537,563</td><td>18</td></tr>
    
        <tr><td class="place">31</td><td></td><td><a href="/team/199510">BKISC</a></td><td class="country"><a href="/stats/2024/VN"><img src="/static/images/sf/vn.svg" alt="VN"></a></td><td>518,575</td><td>70</td></tr>
    
        <tr><td class="place">32</td><td></td><td><a href="/team/550">FAUST</a></td><td class="country"><a href="/stats/2024/DE"><img src="/static/images/sf/de.svg" alt="DE"></a></td><td>517,318</td><td>21</td></tr>
    
        <tr><td class="place">33</td><td></td><td><a href="/team/4419">0ops</a></td><td class="country"><a href="/stats/2024/CN"><img src="/static/images/sf/cn.svg" alt="CN"></a></td><td>495,784</td><td>14</td></tr>
    
        <tr><td class="place">34</td><td></td><td><a href="/team/116280">CyberSpace</a></td><td class="country"><a href="/stats/2024/US"><img src="/static/images/sf/us.svg" alt="US"></a></td><td>491,594</td><td>70</td></tr>
    
        <tr><td class="place">35</td><td></td><td><a href="/team/1964">WE_0WN_Y0U</a></td><td class="country"><a href="/stats/2024/AT"><img src="/static/images/sf/at.svg" alt="AT"></a></td><td>486,189</td><td>23</td></tr>
    
        <tr><td class="place">36</td><td></td><td><a href="/team/300">Tower of Hanoi</a></td><td class="country"><a href="/stats/2024/IT"><img src="/static/images/sf/it.svg" alt="IT"></a></td><td>477,462</td><td>43</td></tr>
    
        <tr><td class="place">37</td><td></td><td><a href="/team/16691">InfoSecIITR</a></td><td class="country"><a href="/stats/2024/IN"><img src="/static/images/sf/in.svg" alt="IN"></a></td><td>475,669</td><td>80</td></tr>
    
        <tr><td class="place">38</td><td></td><td><a href="/team/303153">The Awakening of Ancient Spirits</a></td><td class="country"><a href="/stats/2024/TR"><img src="/static/images/sf/tr.svg" alt="TR"></a></td><td>474,847</td><td>22</td></tr>
    
        <tr><td class="place">39</td><td></td><td><a href="/team/1005">More Smoked Leet Chicken</a></td><td class="country"><a href="/stats/2024/RU"><img src="/static/images/sf/ru.svg" alt="RU"></a></td><td>470,921</td><td>19</td></tr>
    
        <tr><td class="place">40</td><td></td><td><a href="/team/585">hxp</a></td><td class="country"></td><td>470,734</td><td>13</td></tr>
    
        <tr><td class="place">41</td><td></td><td><a href="/team/15337">saarsec</a></td><td class="country"><a href="/stats/2024/DE"><img src="/static/images/sf/de.svg" alt="DE"></a></td><td>467,540</td><td>7</td></tr>
    
        <tr><td class="place">42</td><td></td><td><a href="/team/7221">KITCTF</a></td><td class="country"><a href="/stats/2024/DE"><img src="/static/images/sf/de.svg" alt="DE"></a></td><td>466,345</td><td>23</td></tr>
    
        <tr><td class="place">43</td><td></td><td><a href="/team/140885">The Few Chosen</a></td><td class="country"><a href="/stats/2024/RO"><img src="/static/images/sf/ro.svg" alt="RO"></a></td><td>458,812</td><td>20</td></tr>
    
        <tr><td class="place">44</td><td></td><td><a href="/team/166729">les amateurs</a></td><td class="country"><a href="/stats/2024/US"><img src="/static/images/sf/us.svg" alt="US"></a></td><td>452,794</td><td>15</td></tr>
    
        <tr><td class="place">45</td><td></td><td><a href="/team/193591">Maple Mallard Magistrates</a></td><td class="country"></td><td>444,115</td><td>5</td></tr>
    
        <tr><td class="place">46</td><td></td><td><a href="/team/46516">TheRomanXpl0it</a></td><td class="country"><a href="/stats/2024/IT"><img src="/static/images/sf/it.svg" alt="IT"></a></td><td>443,100</td><td>62</td></tr>
    
        <tr><td class="place">47</td><td></td><td><a href="/team/268941">*0xA</a></td><td class="country"><a href="/stats/2024/CN"><img src="/static/images/sf/cn.svg" alt="CN"></a></td><td>442,413</td><td>11</td></tr>
    
        <tr><td class="place">48</td><td></td><td><a href="/team/109611">IQ-toppene</a></td><td class="country"><a href="/stats/2024/NO"><img src="/static/images/sf/no.svg" alt="NO"></a></td><td>431,799</td><td>36</td></tr>
    
        <tr><td class="place">49</td><td></td><td><a href="/team/57908">WreckTheLine</a></td><td class="country"></td><td>431,420</td><td>12</td></tr>
    
        <tr><td class="place">50</td><td></td><td><a href="/team/70159">HCS</a></td><td class="country"><a href="/stats/2024/ID"><img src="/static/images/sf/id.svg" alt="ID"></a></td><td>428,759</td><td>95</td></tr>
    
    </tbody></table>



    
    <div class="container">
        <ul class="pagination pagination-sm">
        
            <li class="disabled prev"><a href="#">‹‹ Prev</a></li>
        
        
        
            
                
                    <li class="current page active"><a href="#">1</a></li>
                
            
        
            
                
                    <li><a href="/stats/2024?page=2" class="page">2</a></li>
                
            
        
            
                
                    <li><a href="/stats/2024?page=3" class="page">3</a></li>
                
            
        
            
                
                    <li><a href="/stats/2024?page=4" class="page">4</a></li>
                
            
        
            
                
                    <li><a href="/stats/2024?page=5" class="page">5</a></li>
                
            
        
            
                
                    <li><a href="/stats/2024?page=6" class="page">6</a></li>
                
            
        
        
            <li class="disabled prev"><a href="#">...</a></li>
        
        
            <li><a href="/stats/2024?page=2" class="next">Next ››</a></li>
        
        </ul>
    </div>
    

<div class="page-header">
<h2>Top 10 countries by team count</h2>
</div>
<div class="container">
<ul>

<li style="list-style-type: none;">
    
    <img src="/static/images/sf/us.svg" alt="US" width="16px">&nbsp;US
    
    — 5981
    
</li>

<li style="list-style-type: none;">
    
    <img src="/static/images/sf/in.svg" alt="IN" width="16px">&nbsp;IN
    
    — 5315
    
</li>

<li style="list-style-type: none;">
    
    <img src="/static/images/sf/ru.svg" alt="RU" width="16px">&nbsp;RU
    
    — 2335
    
</li>

<li style="list-style-type: none;">
    
    <img src="/static/images/sf/cn.svg" alt="CN" width="16px">&nbsp;CN
    
    — 1713
    
</li>

<li style="list-style-type: none;">
    
    <img src="/static/images/sf/fr.svg" alt="FR" width="16px">&nbsp;FR
    
    — 1687
    
</li>

<li style="list-style-type: none;">
    
    <img src="/static/images/sf/id.svg" alt="ID" width="16px">&nbsp;ID
    
    — 1562
    
</li>

<li style="list-style-type: none;">
    
    <img src="/static/images/sf/vn.svg" alt="VN" width="16px">&nbsp;VN
    
    — 1499
    
</li>

<li style="list-style-type: none;">
    
    <img src="/static/images/sf/de.svg" alt="DE" width="16px">&nbsp;DE
    
    — 1163
    
</li>

<li style="list-style-type: none;">
    
    <img src="/static/images/sf/kr.svg" alt="KR" width="16px">&nbsp;KR
    
    — 1155
    
</li>

<li style="list-style-type: none;">
    
    <img src="/static/images/sf/jp.svg" alt="JP" width="16px">&nbsp;JP
    
    — 1155
    
</li>

</ul>
<p>999 teams total</p>
</div>

<script type="text/javascript">
$(function() {
    $('.typeahead').typeahead({
        limit: 20,
        name: 'teams',
        remote: '/team/list/?q=%QUERY'
    });
})
</script>



        <div class="modal hide fade" id="loginModal">
    <div class="modal-header">
        <button class="close" data-dismiss="modal">x</button>
        <h3>Sign in with : </h3>
    </div>
    <div class="modal-body" align="center">
       
        
    </div>
    </div>


  <div class="row">
    <div class="span4">
    </div>
  </div>

    </div>


    <footer class="footer">
    <div class="container">
      <p class="pull-right"><iframe id="twitter-widget-0" scrolling="no" frameborder="0" allowtransparency="true" allowfullscreen="true" class="twitter-follow-button twitter-follow-button-rendered" style="position: static; visibility: visible; width: 138px; height: 20px;" title="Twitter Follow Button" src="https://platform.twitter.com/widgets/follow_button.2f70fb173b9000da126c79afe2098f02.en.html#dnt=false&amp;id=twitter-widget-0&amp;lang=en&amp;screen_name=CTFtime&amp;show_count=false&amp;show_screen_name=true&amp;size=m&amp;time=1736875992715" data-screen-name="CTFtime"></iframe>        <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script></p>
      <p>© 2012 — 2024 CTFtime team.</p><p>All tasks and writeups are copyrighted by their respective authors. <a href="/privacy"></a>.<br>
    Hosting provided by <a href="http://www.transdata.no/"></a>.</p>
    </div>
    </footer>


    <script src="/static/bootstrap/js/bootstrap-transition.js"></script>
    <script src="/static/bootstrap/js/bootstrap-alert.js"></script>
    <script src="/static/bootstrap/js/bootstrap-modal.js"></script>
    <script src="/static/bootstrap/js/bootstrap-dropdown.js"></script>
<!--    <script src="/static/bootstrap/js/bootstrap-scrollspy.js"></script>-->
    <script src="/static/bootstrap/js/bootstrap-tab.js"></script>
    <script src="/static/bootstrap/js/bootstrap-tooltip.js"></script>
    <script src="/static/bootstrap/js/bootstrap-popover.js"></script>
    <script src="/static/bootstrap/js/bootstrap-button.js"></script>
    <script src="/static/bootstrap/js/bootstrap-collapse.js"></script>
<!--    <script src="/static/bootstrap/js/bootstrap-carousel.js"></script>-->
    <script src="/static/js/typeahead_f.js"></script>

    <script type="text/javascript">
        $('.dropdown-toggle').dropdown();

        window.addEventListener("load", function () {
            window.cookieconsent.initialise({
                "palette": {
                    "popup": {
                        "background": "#efefef",
                        "text": "#404040"
                    },
                    "button": {
                        "background": "#fb0505"
                    }
                },
                "position": "bottom-right",
                "content": {
                    "message": "This website uses cookies to manage authentication, for analytics, and other functions.",
                    "link": "Privacy policy",
                    "href": "https://ctftime.org/privacy"
                }
            })
        });
    </script>

<!-- Yandex.Metrika counter -->
<script type="text/javascript">
(function (d, w, c) {
    (w[c] = w[c] || []).push(function() {
        try {
            w.yaCounter14236711 = new Ya.Metrika({id:14236711, enableAll: true, webvisor:true});
        } catch(e) {}
    });
    
    var n = d.getElementsByTagName("script")[0],
        s = d.createElement("script"),
        f = function () { n.parentNode.insertBefore(s, n); };
    s.type = "text/javascript";
    s.async = true;
    s.src = (d.location.protocol == "https:" ? "https:" : "http:") + "//mc.yandex.ru/metrika/watch.js";

    if (w.opera == "[object Opera]") {
        d.addEventListener("DOMContentLoaded", f);
    } else { f(); }
})(document, window, "yandex_metrika_callbacks");
</script>
<noscript><div><img src="//mc.yandex.ru/watch/14236711" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-559211-27']);
  _gaq.push(['_setDomainName', 'ctftime.org']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
  

<div><div class="grecaptcha-badge" data-style="bottomright" style="width: 256px; height: 60px; display: block; transition: right 0.3s; position: fixed; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-h5kl4a47m4sg" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="https://www.google.com/recaptcha/api2/anchor?ar=1&amp;k=6Lfl-uUUAAAAAFgA71MPRAPNGt8xQjV2C30BsoXT&amp;co=aHR0cHM6Ly9jdGZ0aW1lLm9yZzo0NDM.&amp;hl=ru&amp;v=1Bq_oiMBd4XPUhKDwr0YL1Js&amp;size=invisible&amp;cb=8m0ln4uo6nq2"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe style="display: none;"></iframe></div><iframe scrolling="no" frameborder="0" allowtransparency="true" src="https://platform.twitter.com/widgets/widget_iframe.2f70fb173b9000da126c79afe2098f02.html?origin=https%3A%2F%2Fctftime.org" title="Twitter settings iframe" style="display: none;"></iframe><div id="monica-content-root" class="monica-widget" style="pointer-events: auto;"></div><iframe id="rufous-sandbox" scrolling="no" frameborder="0" allowtransparency="true" allowfullscreen="true" style="position: absolute; visibility: hidden; display: none; width: 0px; height: 0px; padding: 0px; border: none;" title="Twitter analytics iframe"></iframe></body>
    <!--  <div class="modal-header">
        <button class="close" data-dismiss="modal">x</button>
        <h3>Sign in with : </h3>
    </div>
    <div class="modal-body" align="center">
       
        
    </div>
    </div>


  <div class="row">
    <div class="span4">
    </div>
    <div class="modal-header">
        <button class="close" data-dismiss="modal">x</button>
        <h3>Sign in with : </h3>
    </div>
    <div class="modal-body" align="center">
       
        
    </div>
    </div>


  <div class="row">
    <div class="span4">
    </div>
    <div class="modal hide fade" id="loginModal">
    <div class="modal-header">
        <button class="close" data-dismiss="modal">x</button>
        <h3>Sign in with : </h3>
    </div>
    <div class="modal-body" align="center">
       
        
    </div>
    </div>


  <div class="row">
    <div class="span4">
    </div>
  </div>
  
  <div class="modal hide fade" id="loginModal">
    <div class="modal-header">
        <button class="close" data-dismiss="modal">x</button>
        <h3>Sign in with : </h3>
    </div>
    <div class="modal-body" align="center">
       
        
    </div>
    </div>


  <div class="row">
    <div class="{СTFLABS2025}span4">
    </div>
  </div>-->""")

@app.route("/verify", methods=["POST"])
def verify():
    username = request.form["username"]
    user_password = request.form["password"]

    # Проверка логина и пароля
    if username == login and user_password == password:
        return "Correct login! RkxBR3tBU1RBTkFfQ1lCRVJfTEFCU30="
    else:
        return "Incorrect credentials! Try again."

if __name__ == "__main__":
    app.run(debug=True)
