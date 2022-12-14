from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    lists =  [
    {
      "source": {
        "id": "reuters",
        "name": "Reuters"
      },
      "author": "Nathan Frandino",
      "title": "California researchers test everybody in one town for coronavirus - Reuters India",
      "description": "Researchers began testing an entire town in northern California for the novel coronavirus and its antibodies on Monday, one of the first such efforts since the pandemic hit the United States.",
      "url": "https://in.reuters.com/article/health-coronavirus-california-testing-idINKBN22309H",
      "urlToImage": "https://s3.reutersmedia.net/resources/r/?m=02&d=20200421&t=2&i=1515823617&w=1200&r=LYNXMPEG3K05Q",
      "publishedAt": "2020-04-21T06:18:01Z",
      "content": "BOLINAS, Calif. (Reuters) - Researchers began testing an entire town in northern California for the novel coronavirus and its antibodies on Monday, one of the first such efforts since the pandemic hit the United States. \r\nBolinas, a wealthy beach town in Mari… [+2727 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Eletsonline.com"
      },
      "author": "BFSI Network",
      "title": "80% asymptomatic cases deepens COVID-19 concerns in India - Elets",
      "description": "With inflating number of asymptomatic Covid-19 cases responsible for spreading the infection, India's top medical research body is struggling with the problem caused by the \"silent spreaders\" and",
      "url": "https://bfsi.eletsonline.com/80-asymptomatic-cases-deepens-covid-19-concerns-in-india/",
      "urlToImage": "https://mk0bfsieletsonlt96u6.kinstacdn.com/wp-content/uploads/2020/04/80-asymptomatic-cases-deepens-COVID-19-concerns-in-India.jpg",
      "publishedAt": "2020-04-21T06:01:31Z",
      "content": "🔊 Listen to this ArticleWith inflating number of asymptomatic Covid-19 cases responsible for spreading the infection, Indias top medical research body is struggling with the problem caused by the silent spreaders and examining the feasibility of introducing … [+1847 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Indiatoday.in"
      },
      "author": '',
      "title": "From 1 to 9: How AC air spread coronavirus to 3 families at a restaurant in China - dineshr",
      "description": "A family that arrived in China's Guangzhou from Wuhan spread the virus to two other families while dining at a restaurant. The virus transmission happened through the AC airflow.",
      "url": "https://www.indiatoday.in/world/story/how-ac-air-spread-coronavirus-to-3-families-at-a-restaurant-in-china-1669262-2020-04-21",
      "urlToImage": "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202004/2020-04-17T083537Z_1806127465_-647x363.png?0i9XlAO9vhGwC.SPKmavPVrqeVxPRur0",
      "publishedAt": "2020-04-21T05:11:31Z",
      "content": "In January, when the coronavirus epicentre Wuhan was yet to be locked down completely, a family was dining at a restaurant in Guangzhou. The family had come from Wuhan and one of them was carrying the virus unknowingly. Days later, nine others who dined at th… [+2075 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Monitor.co.ug"
      },
      "author": "AFP",
      "title": "Coronavirus: How diseases have originates from the animal world - Daily Monitor",
      "description": "Scientists think it originated in bats and could have been passed on via another mammal like a pangolin, an endangered species whose meat and scales are highly prized in parts of Asia",
      "url": "https://www.monitor.co.ug/News/National/Coronavirus-origin-diseases-animal-world-rabies-malaria/688334-5529986-3buh5a/index.html",
      "urlToImage": "https://www.monitor.co.ug/image/view/-/5530002/medRes/2603017/-/uhea90z/-/latest03pix.jpg",
      "publishedAt": "2020-04-21T05:04:53Z",
      "content": "By AFP \r\nWhether it came from a bat or a pangolin is not certain, but one thing is: the coronavirus outbreak that has killed tens of thousands and turned the world upside down comes from the animal world.\r\nIt is human activity enabled the virus to jump to peo… [+4988 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Theprint.in"
      },
      "author": "Kristen V Brown",
      "title": "Why there is a big debate over accuracy and results of Covid anti-body tests - ThePrint",
      "description": "The anti-body test is crucial to understanding Covid-19 & the virus that causes it. It can tell how many people potentially have some level of immunity.",
      "url": "https://theprint.in/world/why-there-is-a-big-debate-over-accuracy-and-results-of-covid-anti-body-tests/405721/",
      "urlToImage": "https://d2c7ipcroan06u.cloudfront.net/wp-content/uploads/2020/04/Sample-test.jpg",
      "publishedAt": "2020-04-21T04:26:21Z",
      "content": "San Francisco: As the U.S. begins to consider letting people go back to work and lifting social-distancing rules, a new debate over testing is emerging. Researchers are racing to back-fill the gaping holes left by shortfalls in diagnostic tests for currently … [+8536 chars]"
    },
    {
      "source": {
        "id": "cnbc",
        "name": "CNBC"
      },
      "author": '',
      "title": "Coronavirus antibody testing shows LA County outbreak is up to 55 times bigger than reported cases - CNBCTV18",
      "description": "The results are based on antibody testing of about 863 people who were representative of LA County, the researchers said.Get latest Healthcare online at cnbctv18.com",
      "url": "https://www.cnbc.com/2020/04/20/coronavirus-antibody-testing-shows-la-county-outbreak-is-up-to-55-times-bigger-than-reported-cases.html",
      "urlToImage": "https://images.cnbctv18.com/wp-content/uploads/2020/03/coronavirus-gloves-768x502.jpg",
      "publishedAt": "2020-04-21T04:12:12Z",
      "content": "The Covid-19 outbreak in Los Angeles County is likely far more widespread than previously thought, up to an estimated 55 times bigger than the number of confirmed cases, according to new research from the University of Southern California and the LA Departmen… [+2671 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Indiatvnews.com"
      },
      "author": "IANS",
      "title": "Plasma therapy shows positive result on critical COVID-19 patient: Max Hospital - India TV News",
      "description": "The Max Hospital in Saket has administered plasma therapy on a critical coronavirus patient and it's showing positive results with the patient being taken off ventilator support, the hospital said on Monday.",
      "url": "https://www.indiatvnews.com/news/india/plasma-therapy-shows-positive-result-on-critical-covid-19-patient-max-hospital-609670",
      "urlToImage": "https://resize.indiatvnews.com/en/resize/newbucket/715_-/2020/04/800-1-1587441330.jpeg",
      "publishedAt": "2020-04-21T04:10:41Z",
      "content": "Image Source : AP Plasma therapy shows positive result on critical Covid-19 patient: Max Hospital\r\nThe Max Hospital in Saket has administered plasma therapy on a critical coronavirus patient and it's showing positive results with the patient being taken off v… [+3522 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Daijiworld.com"
      },
      "author": '',
      "title": "Ireland reports record high of COVID-19 deaths in single day - Daijiworld.com",
      "description": "",
      "url": "https://www.daijiworld.com/news/newsDisplay.aspx?newsID=699093",
      "urlToImage": "http://daijiworld.com/images/daijiSquareLogo.png",
      "publishedAt": "2020-04-21T03:16:27Z",
      "content": "Dublin, Apr 21 (IANS): A total of 77 COVID-19-related deaths were reported in Ireland on Monday, the highest figure ever recorded in a single day since the COVID-19 outbreak in the country, according to the statistics released by the Irish Department of Healt… [+1089 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Indianexpress.com"
      },
      "author": "Ravish Tiwari",
      "title": "ExplainSpeaking: Covid-19 cases are still growing slowly, but this week is crucial - The Indian Express",
      "description": "A weekly newsletter that will give you a heads-up on the Covid-19 headlines this week — and explain what lies between them.",
      "url": "https://indianexpress.com/article/explained/explain-speaking-covid-19-cases-are-still-growing-slowly-but-this-week-is-crucial-6371150/",
      "urlToImage": "https://images.indianexpress.com/2020/04/explain-speaking-759.jpg?w=759",
      "publishedAt": "2020-04-21T02:44:40Z",
      "content": "Written by Ravish Tiwari\r\n | New Delhi | \r\nUpdated: April 21, 2020 8:09:24 am\r\nThis week will be crucial for the government to understand the dynamics of the gradual unlockdown strategy whether it re-starts economic activity, or ends up compromising the gains… [+4094 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Firstpost.com"
      },
      "author": '',
      "title": "Higher levels of nitrogen dioxide in the air might relate to higher Coronavirus death rates - Firstpost",
      "description": "Nitrogen dioxide damages the human respiratory tract and it has been known to cause respiratory and cardiovascular diseases in humans.",
      "url": "https://www.firstpost.com/tech/science/higher-levels-of-nitrogen-dioxide-in-the-air-might-relate-to-higher-coronavirus-death-rates-8281111.html",
      "urlToImage": "https://images.firstpost.com/wp-content/uploads/2019/12/screencapture-storage-googleapis-afs-prod-media-b1c8a3fb79e24b4f90971bb5ed56ffa8-1000-jpeg-2019-12-05-10_59_58.jpg",
      "publishedAt": "2020-04-21T02:34:58Z",
      "content": "Press Trust of IndiaApr 21, 2020 08:04:58 IST\r\nHigher levels of nitrogen dioxide pollutants in the air may be associated with an increased number of deaths from COVID-19, according to a study.\r\nThe research, published in the journal Science of the Total Envir… [+3471 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Hindustantimes.com"
      },
      "author": "Sanchita Sharma",
      "title": "Covid-19 not the last pandemic, world has to build resilience - Hindustan Times",
      "description": "The coronavirus disease (Covid-19), which has already infected 2.4 million people and killed at least 165,000, is the second most devastating pandemic after the 1918 Spanish flu.",
      "url": "https://www.hindustantimes.com/india-news/covid-not-the-last-pandemic-world-has-to-build-resilience/story-bOrpRseqzhDgTjvxStRFzK.html",
      "urlToImage": "https://www.hindustantimes.com/rf/image_size_960x540/HT/p2/2020/04/21/Pictures/_1d79ff1c-8347-11ea-a351-6978c1d205f3.png",
      "publishedAt": "2020-04-21T00:51:42Z",
      "content": "Covid-19 is not the first, nor will it be the last , of high-impact, rapidly spreading pandemics to cause disruption and death on a large scale, upend economies, and roil society. Pandemics are emerging with higher frequency and becoming increasingly difficul… [+5248 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Menafn.com"
      },
      "author": "MENAFN",
      "title": "Oxford University to Begin Tests of its Coronavirus Vaccine on Humans NEXT WEEK in Hope of Having a Jab Ready for Autumn - MENAFN.COM",
      "description": "(MENAFN - SomTribune) Hopes of eliminating the coronavirus were raised today after leading British experts revealed trials of a vaccine would begin on humans next week.\nOxford University scientists are confident they can get jab for the incurable disease roll…",
      "url": "https://menafn.com/1100056200/Oxford-University-to-Begin-Tests-of-its-Coronavirus-Vaccine-on-Humans-NEXT-WEEK-in-Hope-of-Having-a-Jab-Ready-for-Autumn",
      "urlToImage": "https://menafn.com/updates/pr/2020-04/20/S_af424335-cimage_story.jpg",
      "publishedAt": "2020-04-21T00:08:28Z",
      "content": "(MENAFN - SomTribune) Hopes of eliminating the coronavirus were raised today after leading British experts revealed trials of a vaccine would begin on humans next week.\r\nOxford University scientists are confident they can get jab for the incurable disease rol… [+5519 chars]"
    },
    {
      "source": {
        "id": "the-times-of-india",
        "name": "The Times of India"
      },
      "author": "Times Of India",
      "title": "Plasma of asymptomatic donors may not help - Times of India",
      "description": "CHENNAI: With many states showing intent to test plasma therapy, medical experts say the procedure may be a shot in the dark for treating Covid-19 pat.",
      "url": "https://timesofindia.indiatimes.com/city/chennai/plasma-of-asymptomatic-donors-may-not-help/articleshow/75261086.cms",
      "urlToImage": "https://static.toiimg.com/thumb/msid-47529300,width-1070,height-580,imgsize-110164,resizemode-75,overlay-toi_sw,pt-32,y_pad-40/photo.jpg",
      "publishedAt": "2020-04-20T22:40:00Z",
      "content": "Subscribe\r\nStart Your Daily Mornings with Times of India Newspaper!Order Now"
    },
    {
      "source": {
        "id": '',
        "name": "Dailymail.co.uk"
      },
      "author": "By Mary Kekatos Senior Health Reporter For Dailymail.com",
      "title": "Coronavirus HAS mutated: Strains that evolved to be far deadlier have spread in Europe and New York - Daily Mail",
      "description": "Some of the deadliest mutations were Zhejiang, where the university is located, as well as in several European countries, but milder mutations were the varieties found in the US.",
      "url": "https://www.dailymail.co.uk/health/article-8237849/Coronavirus-mutated-Strains-evolved-far-deadlier-spread-Europe-New-York.html",
      "urlToImage": "https://i.dailymail.co.uk/1s/2020/04/20/20/27430266-0-image-a-26_1587410581103.jpg",
      "publishedAt": "2020-04-20T22:36:02Z",
      "content": "The novel coronavirus has mutated which could have very deadly complications for the pandemic, a new small study finds.\r\nA team of Chinese researchers from Zhejiang University say there are at least 30 strains of the virus, known as SARS-COV-2.\r\nStrains withi… [+6115 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Thelancet.com"
      },
      "author": '',
      "title": "Safety and immunogenicity of a candidate Middle East respiratory syndrome coronavirus viral-vectored vaccine: a dose-escalation, open-label, non-randomised, uncontrolled, phase 1 trial - The Lancet",
      "description": "ChAdOx1 MERS was safe and well tolerated at all tested doses. A single dose was able\nto elicit both humoral and cellular responses against MERS-CoV. The results of this\nfirst-in-human clinical trial support clinical development progression into field\nphase 1b…",
      "url": "https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(20)30160-2/fulltext",
      "urlToImage": "//els-jbs-prod-cdn.jbs.elsevierhealth.com/cms/asset/e5280193-8792-4398-84be-fda0608068ec/gr2.jpg",
      "publishedAt": "2020-04-20T22:35:42Z",
      "content": "We use cookies to help provide and enhance our service and tailor content and ads. By continuing you agree to the use of cookies.\r\nCopyright © 2020 Elsevier Inc. except certain content provided by third parties.\r\nPrivacy Policy   Terms and Conditions"
    },
    {
      "source": {
        "id": '',
        "name": "Youtube.com"
      },
      "author": '',
      "title": "City of Jackson setting up COVID-19 symptom collector - 16 WAPT News Jackson",
      "description": "The City of Jackson is one of the first municipalities in the world to utilize a COVID-19 early detection tool to help combat the spread of the deadly virus....",
      "url": "https://www.youtube.com/watch?v=R3dKwhGb5OY",
      "urlToImage": "https://i.ytimg.com/vi/R3dKwhGb5OY/maxresdefault.jpg",
      "publishedAt": "2020-04-20T22:29:19Z",
      "content": "The City of Jackson is one of the first municipalities in the world to utilize a COVID-19 early detection tool to help combat the spread of the deadly virus.\r\nSubscribe to WAPT on YouTube now for more: http://bit.ly/1hYcJNa\r\nGet more Jackson news: http://www.… [+132 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Bbc.com"
      },
      "author": "https://www.facebook.com/bbcnews",
      "title": "Coronavirus: Derby consultant Manjeet Singh Riyat dies - BBC News",
      "description": "Manjeet Singh Riyat was described as \"well loved\" and \"hugely respected\" throughout the NHS.",
      "url": "https://www.bbc.com/news/uk-england-derbyshire-52362791",
      "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/13E3A/production/_111866418_manjeetsingh.jpg",
      "publishedAt": "2020-04-20T21:29:05Z",
      "content": "Image copyrightUHDBImage caption\r\n Dr Manjeet Singh Riyat was described as an \"incredibly charming person\" who will be missed \"immensely\"\r\nAn accident and emergency consultant who was \"hugely respected\" nationally has died after contracting coronavirus.\r\nMr M… [+1310 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Bloombergquint.com"
      },
      "author": "Robert Langreth",
      "title": "Americans Are Poisoning Themselves in Their Rush to Fight Virus - BloombergQuint",
      "description": "Coronavirus Cleaning Goes Haywire With Grim Surge in Poisonings",
      "url": "https://www.bloombergquint.com/business/coronavirus-cleaning-goes-haywire-with-grim-surge-in-poisonings",
      "urlToImage": "https://images.assettype.com/bloombergquint%2F2018-08%2F3a8e2237-2edb-4494-bcf2-231993fb6108%2FBLOOMBERG_LOGO.png?rect=0%2C56%2C1920%2C1008&w=1200&auto=format%2Ccompress&ogImage=true",
      "publishedAt": "2020-04-20T20:35:05Z",
      "content": "(Bloomberg) -- Poisonings related to cleaners and disinfectants surged in the U.S. last month as the global pandemic spurred a haphazard rush to disinfect everything."
    },
    {
      "source": {
        "id": '',
        "name": "Youtube.com"
      },
      "author": '',
      "title": "UK COVID-19 death toll rises to 16509 after 449 more people die in lowest increase for a fortnight - The Sun",
      "description": "Coronavirus latest -The UK coronavirus death toll today rose to 16,509 after 449 more fatalities were recorded in the lowest increase for a fortnight. The la...",
      "url": "https://www.youtube.com/watch?v=uke5ZI6YK0A",
      "urlToImage": "https://i.ytimg.com/vi/uke5ZI6YK0A/maxresdefault.jpg",
      "publishedAt": "2020-04-20T20:23:48Z",
      "content": "Coronavirus latest -The UK coronavirus death toll today rose to 16,509 after 449 more fatalities were recorded in the lowest increase for a fortnight.\r\nThe last time the daily death toll was that low was two weeks ago on April 6 when 439 fatalities were repor… [+1113 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Thequint.com"
      },
      "author": "Sushovan Sircar",
      "title": "Mathematical Models Warn Several Lockdowns Needed to Beat COVID-19 - The Quint",
      "description": "Dr Rajesh Singh, mathematician at Cambridge University, along with Dr R Adhikari of IMS, Chennai told The Quint that the time horizon for an exit strategy (post COVID-19 lockdown) may take at least one year.",
      "url": "https://www.thequint.com/news/india/scientists-mathematical-modeling-warn-sustained-lockdowns-to-beat-covid-19",
      "urlToImage": "https://images.assettype.com/thequint/2020-04/a000e1eb-c4fa-469c-b1a9-c22064e3d836/corona_chain.jpg",
      "publishedAt": "2020-04-20T20:00:56Z",
      "content": "Scientists who had conducted recent mathematical modelings of the spread of COVID-19 in India say Prime Minister Narendra Modis announcement of an extension of the nationwide lockdown is a vindication of their predictions.\r\nAt the commencement of the lockdown… [+545 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Theguardian.com"
      },
      "author": "Robert Booth",
      "title": "UK care home bosses call for help from medics as death toll grows - The Guardian",
      "description": "Five of the largest care home providers have now recorded a total of at least 1,052 deaths",
      "url": "https://www.theguardian.com/society/2020/apr/20/uk-care-home-bosses-call-for-help-from-medics-as-death-toll-grows",
      "urlToImage": "https://i.guim.co.uk/img/media/563fbccdf1756de277b52d7331ca5d5fa296266a/0_93_4000_2401/master/4000.jpg?width=1200&height=630&quality=85&auto=format&fit=crop&overlay-align=bottom%2Cleft&overlay-width=100p&overlay-base64=L2ltZy9zdGF0aWMvb3ZlcmxheXMvdGctZGVmYXVsdC5wbmc&enable=upscale&s=d26c71b588056a908fb25c2db10e4500",
      "publishedAt": "2020-04-20T18:00:54Z",
      "content": "Doctors and nurses must urgently be deployed to fight coronavirus in care homes, care bosses have said, as the largest operators announced sharp rises in their death tolls.\r\nCare UK, which runs 122 homes in England and Scotland, revealed a 65% increase in dea… [+4390 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Timesofisrael.com"
      },
      "author": '',
      "title": "US grants Israeli prof a patent for tech that could lead to virus vaccine - The Times of Israel",
      "description": "Tel Aviv University's Jonathan Gershoni says his technology targets the mechanism coronavirus uses to infiltrate human cells, making it particularly effective",
      "url": "https://www.timesofisrael.com/us-grants-israeli-prof-patent-for-tech-that-could-see-virus-vaccine-in-months/",
      "urlToImage": "https://static.timesofisrael.com/www/uploads/2020/04/F200417OF17-1-1024x640.jpg",
      "publishedAt": "2020-04-20T17:49:00Z",
      "content": "The United States Patent and Trademark Office has granted a researcher at Tel Aviv University a patent for technology that he says could lead to the development of a vaccine for COVID-19 in a matter of months.\r\n“The vaccine targets the novel coronaviruss Achi… [+2351 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Livemint.com"
      },
      "author": "IANS",
      "title": "Facebook unveils first Covid-19 interactive 'heat maps', set to expand globally - Livemint",
      "description": "Facebook released its first county-by-county map of the US, which shows an estimated percentage of people with Covid-19 symptoms, not confirmed cases.According to Facebook, the maps are meant to help health officials allocate resources and decide where parts …",
      "url": "https://www.livemint.com/technology/tech-news/facebook-unveils-first-covid-19-interactive-heat-maps-set-to-expand-globally-11587403539065.html",
      "urlToImage": "https://images.livemint.com/img/2020/04/20/600x338/facebook_1587404052318_1587404052775.JPG",
      "publishedAt": "2020-04-20T17:36:09Z",
      "content": "San Francisco: Using aggregated public data from a survey conducted by Carnegie Mellon University, Facebook on Monday released its first county-by-county map of the US showing prevalence of self-reported COVID-19 symptoms, adding that such maps will soon be r… [+3497 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Orissapost.com"
      },
      "author": "Post News Network",
      "title": "Good news: Anti-viral drug ‘Remdesivir’ brings some hope for coronavirus-stricken world - OrissaPOST",
      "description": "Houston: Researchers have claimed that COVID-19 patients in a clinical trial are responding quickly to ‘Remdesivir’. They said this finding is ‘promising’. However, they also emphasized the need for more trials to test the effectiveness of the anti-viral drug…",
      "url": "https://www.orissapost.com/good-news-anti-viral-drug-remdesivir-brings-some-hope-for-coronavirus-stricken-world/",
      "urlToImage": "https://www.orissapost.com/wp-content/uploads/2020/04/‘Remdesivir’.jpg",
      "publishedAt": "2020-04-20T17:31:22Z",
      "content": "Houston: Researchers have claimed that COVID-19 patients in a clinical trial are responding quickly to Remdesivir. They said this finding is promising. However, they also emphasized the need for more trials to test the effectiveness of the anti-viral drug.\r\nR… [+3026 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Indianewengland.com"
      },
      "author": '',
      "title": "Maternal hypertensive disorders bad for kids' mental health - India New England",
      "description": "London– Hypertensive pregnancy disorders, especially preeclampsia, a form of high blood pressure during pregnancy, may lead to adverse mental health conditions in children, say researchers. A…",
      "url": "https://indianewengland.com/2020/04/maternal-hypertensive-disorders-bad-for-kids-mental-health/",
      "urlToImage": "https://indianewengland.com/wp-content/uploads/2017/11/qtq80-dxxQDB-e1514845548139.jpeg",
      "publishedAt": "2020-04-20T17:07:02Z",
      "content": "London– Hypertensive pregnancy disorders, especially preeclampsia, a form of high blood pressure during pregnancy, may lead to adverse mental health conditions in children, say researchers.\r\nA Finnish study, published in the journal Hypertension, of 4,743 mot… [+2198 chars]"
    },
    {
      "source": {
        "id": "reuters",
        "name": "Reuters"
      },
      "author": "Reuters Editorial",
      "title": "New York nurses sue state and two hospitals over 'inadequate' virus protection - Reuters",
      "description": "The New York State Nurses Association sued the state and two hospitals on Monday to force them to provide equipment and adopt safety measures to prevent the spread of COVID-19 among the association's members in the hard-hit state.",
      "url": "https://in.reuters.com/article/health-coronavirus-usa-nurses-idINL1N2C80SX",
      "urlToImage": "https://s4.reutersmedia.net/resources_v2/images/rcom-default.png",
      "publishedAt": "2020-04-20T16:40:00Z",
      "content": "April 20 (Reuters) - The New York State Nurses Association sued the state and two hospitals on Monday to force them to provide equipment and adopt safety measures to prevent the spread of COVID-19 among the association’s members in the hard-hit state. \r\nThe a… [+1795 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Businessinsider.in"
      },
      "author": "Business Insider India",
      "title": "French case raises questions over coronavirus child spread - Business Insider India",
      "description": "Lyon, Apr 20 (AFP) A nine-year-old who contracted COVID-19 in eastern France did not pass the virus on to any other pupils at three ski-schools, according",
      "url": "https://www.businessinsider.in/international/news/french-case-raises-questions-over-coronavirus-child-spread/articleshow/75257318.cms",
      "urlToImage": "https://www.businessinsider.in/photo/75257318/french-case-raises-questions-over-coronavirus-child-spread.jpg?imgsize=64457",
      "publishedAt": "2020-04-20T16:36:00Z",
      "content": "Lyon, Apr 20 (AFP) A nine-year-old who contracted COVID-19 in eastern France did not pass the virus on to any other pupils at three ski-schools, according to new research that suggests infants are not large spreaders of the disease.The child was infected in F… [+1494 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Sci-news.com"
      },
      "author": '',
      "title": "Scientists Propose New Approach to Analyze Genetic Sequences of SARS-CoV-2 Coronavirus | Astronomy - Sci-News.com",
      "description": "Researchers at the Commonwealth Scientific and Industrial Research Organisation (CSIRO) have developed a new visualization platform, underpinned by bioinformatics algorithms originally used to analyze the human genome, to pinpoint differences among the thousa…",
      "url": "http://www.sci-news.com/astronomy/genetic-sequences-sars-cov-2-08343.html",
      "urlToImage": "http://cdn.sci-news.com/images/2020/04/image_8309-Coronavirus.jpg",
      "publishedAt": "2020-04-20T16:02:11Z",
      "content": "Researchers at the Commonwealth Scientific and Industrial Research Organisation (CSIRO) have developed a new visualization platform, underpinned by bioinformatics algorithms originally used to analyze the human genome, to pinpoint differences among the thousa… [+2937 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Cgtn.com"
      },
      "author": "",
      "title": "How AIDS vaccine research could help fight COVID-19 - CGTN",
      "description": "Scientists in California explain how research into vaccines for snake bites and HIV could be the answer to the coronavirus pandemic.",
      "url": "https://newseu.cgtn.com/news/2020-04-20/How-AIDS-vaccine-research-could-help-fight-COVID-19-PQM6DhPSuc/index.html",
      "urlToImage": "https://newseu.cgtn.com/news/324d7a4e7a63544f78636a4e796b444f7a63444f31457a6333566d54/img/8052d2db16e042aa90c2eb4016af3739/8052d2db16e042aa90c2eb4016af3739-1.jpg",
      "publishedAt": "2020-04-20T15:50:52Z",
      "content": "The race is on to develop a COVID-19 vaccine from the blood of survivors. Scientists from around the world are working together to find an effective antibody against the virus that could also treat the diverse coronavirus family. \r\nAntibodies are a protein pr… [+1087 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Moneycontrol.com"
      },
      "author": '',
      "title": "Coronavirus pandemic | Boston Globe prints 16 pages of obituaries - Moneycontrol",
      "description": "Several Twitter users took to the social media platform to discuss how they have never seen obituary listings take up so many pages of a newspaper.",
      "url": "https://www.moneycontrol.com/news/world/coronavirus-pandemic-boston-globe-prints-16-pages-of-obituaries-5168921.html",
      "urlToImage": "https://static-news.moneycontrol.com/static-mcnews/2020/04/3-coronavirus-robots-770x433.jpg",
      "publishedAt": "2020-04-20T15:29:23Z",
      "content": "Readers got a deeper insight into the global health crisis that the world is battling at present, especially America -- which is engaged in a tedious fight to contain the number of novel coronavirus cases when a leading daily published a list of obituaries th… [+2141 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Ultimateclassicrock.com"
      },
      "author": "coreyirwin",
      "title": "14 Smokin' Rock Star Marijuana Stories - Ultimate Classic Rock",
      "description": "A roundup of famous stories about rockers and weed, featuring the Beatles, Lynyrd Skynyrd, David Lee Roth, Robert Plant and others.",
      "url": "https://ultimateclassicrock.com/weed-stories/",
      "urlToImage": "https://townsquare.media/site/295/files/2020/04/Pot-stories-collage.jpg?w=1200&h=0&zc=1&s=0&a=t&q=89",
      "publishedAt": "2020-04-20T15:28:00Z",
      "content": "Weed, pot, grass, chronic - whatever name you want to give it, theres no denying the long history between marijuana and music.\r\nThe narcotic has reportedly inspired many artists to pen some of their most imaginative works. While the drug is arguably most link… [+12255 chars]"
    },
    {
      "source": {
        "id": "the-times-of-india",
        "name": "The Times of India"
      },
      "author": "monitkhanna",
      "title": "Indian-Origin Doctors In US Have Sacrificed Their Lives Fighting COVID-19 Pandemic - India Times",
      "description": "Several Indian origin doctors in the US have sacrificed their lives to the novel coronavirus. This has been brought to light by the Indian-American community leaders who state that a considerable number of Indian-origin doctors have gotten infected during thi…",
      "url": "https://www.indiatimes.com/technology/science-and-future/indian-origin-doctors-in-us-have-sacrificed-their-lives-fighting-covid-19-pandemic-511333.html",
      "urlToImage": "https://im.indiatimes.in/content/2020/Apr/FB-Image-Quote_5e9dc0acd270e.jpg",
      "publishedAt": "2020-04-20T15:25:01Z",
      "content": "While the whole world is dealing with the wrath of COVID-19, the whole ordeal has been more terrible for doctors and medical practitioners in the front line who are risking their lives while trying to treat people with the novel coronavirus.\r\nReuters\r\nAnd a r… [+2071 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Livemint.com"
      },
      "author": "Srishti Choudhary",
      "title": "CSIR to test its new sepsis drug for severe patients of Covid-19 - Livemint",
      "description": "According to scientists, there are some clinical similarities between patients suffering from gram-negative Sepsis and Covid-19.The drug has recently been approved for marketing in India and would be available commercially as Sepsivac® from Ahmedabad-based Ca…",
      "url": "https://www.livemint.com/science/health/csir-to-test-its-new-sepsis-drug-for-severe-patients-of-covid-19-11587394617832.html",
      "urlToImage": "https://images.livemint.com/img/2020/04/20/600x338/CSIR_1585851213110_1587394826417.jpg",
      "publishedAt": "2020-04-20T15:04:48Z",
      "content": "NEW DELHI :\r\nRaising hopes for a potential treatment of Covid-19, Indias premier research organization Council of Scientific and Industrial Research (CSIR) has decided to test its new drug against Sepsis to treat critical patients of Covid-19.The drug has rec… [+2688 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Edexlive.com"
      },
      "author": "Edex Live",
      "title": "Researchers develop tool to predict risk of death for people suffering from dementia - EdexLive",
      "description": "The tool asks simple questions about the person during diagnosis and translates it to the chance of dying and of entering a nursing home",
      "url": "https://www.edexlive.com/news/2020/apr/20/researchers-develop-tool-to-predict-risk-of-death-for-people-suffering-from-dementia-11445.html",
      "urlToImage": "https://images.edexlive.com/uploads/user/imagelibrary/2020/4/20/w600X390/download_2.jpg",
      "publishedAt": "2020-04-20T14:55:42Z",
      "content": "Researchers have developed a tool to predict the risk of death and admission to a long-term care facility for patients with dementia. The tool may help conversations between health care providers, patients, and their families, according to the study which has… [+2891 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Newindianexpress.com"
      },
      "author": "Sumi Sukanaya Dutta",
      "title": "Marginally higher than flu: COVID-19 mortality rate in India just 0.41%, estimates study - The New Indian Express",
      "description": "The study has assessed that only 6 per cent of the actual COVID-19 cases are detected globally and this figure varies significantly across countries.",
      "url": "https://www.newindianexpress.com/lifestyle/health/2020/apr/20/marginally-higher-than-flu-covid-19-mortality-rate-in-india-just-041-estimates-study-2132893.html",
      "urlToImage": "https://images.newindianexpress.com/uploads/user/imagelibrary/2020/4/20/w600X390/Corona_Bhubaneshwar_EPS03.jpg",
      "publishedAt": "2020-04-20T14:39:00Z",
      "content": "NEW DELHI: India may have over 1.32 lakh coronavirus patients as on Monday -- nearly seven times the official figure of less than 18,000 cases. This is as per a calculation based on age-specific infection fatality rates and deaths reported in the country so f… [+2782 chars]"
    },
    {
      "source": {
        "id": "fortune",
        "name": "Fortune"
      },
      "author": "David Meyer",
      "title": "Controversy around privacy splits Europe’s push to build COVID-19 contact-tracing apps - Fortune",
      "description": "\"It is vital that...we do not create a tool that enables large-scale data collection on the population, either now or at a later time,\" critics of a leading European contact-tracing platform warn.",
      "url": "https://fortune.com/2020/04/20/coronavirus-contact-tracing-privacy-europe-pepp-pt-dp3t-covid-19-tracking/",
      "urlToImage": "https://content.fortune.com/wp-content/uploads/2020/04/GettyImages-1219900380.jpg?resize=1200,600",
      "publishedAt": "2020-04-20T14:26:04Z",
      "content": ''
    },
    {
      "source": {
        "id": '',
        "name": "Medscape.com"
      },
      "author": '',
      "title": "Pay Attention to In-Hospital Glucose to Save Lives in COVID-19 - Medscape",
      "description": "Mortality was raised fourfold for those with diabetes and sevenfold among those with hyperglycemia but no diabetes history. Clinicians could save more lives by tuning in to this key aspect of care.",
      "url": "https://www.medscape.com/viewarticle/928962",
      "urlToImage": "https://img.medscape.com/thumbnail_library/dt_200420_glucose_level_meter_800x450.jpg",
      "publishedAt": "2020-04-20T14:16:08Z",
      "content": "Editor's note: Find the latest COVID-19 news and guidance in Medscape's Coronavirus Resource Center.\r\nDiabetes and hyperglycemia among people without prior diabetes are strong predictors of mortality among hospitalized patients with COVID-19, new research sug… [+5257 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Tribuneindia.com"
      },
      "author": "Tribune India",
      "title": "Nobel winning scientist claims COVID-19 virus was man made in Wuhan lab: Report - The Tribune",
      "description": "",
      "url": "https://www.tribuneindia.com/news/world/nobel-winning-scientist-claims-covid-19-virus-was-man-made-in-wuhan-lab-report-73697",
      "urlToImage": "https://cms.tribuneindia.com/gallary_content/2020/4/2020_4$largeimg_1841997850.JPG",
      "publishedAt": "2020-04-20T13:11:00Z",
      "content": "Photo for representation only.London, April 20\r\nFrench Nobel prize winning scientist Luc Montagnier has sparked a fresh controversy by claiming that the SARS-CoV-2 virus came from a lab, and is the result of an attempt to manufacture a vaccine against the AID… [+2304 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Kalingatv.com"
      },
      "author": "IANS",
      "title": "Health Ministry speaks about the nature of 80% Covid-19 cases in India - Kalinga TV",
      "description": "New Delhi: The Health Ministry on Monday warned that 80 per cent of all coronavirus patients are asymptomatic or show mild symptoms.\"On the basis of worldwide analysis, out of 100 coronavirus patients, 80 per cent are asymptomatic or show mild sympto",
      "url": "https://kalingatv.com/nation/80-covid-19-cases-are-asymptomatic-or-with-mild-symptoms-health-ministry/",
      "urlToImage": "https://cdn.kalingatv.com/wp-content/uploads/2020/04/Health-Ministry.jpg",
      "publishedAt": "2020-04-20T12:45:00Z",
      "content": "New Delhi: The Health Ministry on Monday warned that 80 per cent of all coronavirus patients are asymptomatic or show mild symptoms.\r\n“On the basis of worldwide analysis, out of 100 coronavirus patients, 80 per cent are asymptomatic or show mild symptoms. Aro… [+491 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Republicworld.com"
      },
      "author": "Aanchal Nigam",
      "title": "US newspaper publishes 15-page obituary as COVID-19 death toll continues to rise - Republic World - Republic World",
      "description": "While Trump claimed that COVID-19 outbreak “passed its peak” in the US, an American newspaper published a 15-page obituary of people who died on April 19.",
      "url": "https://www.republicworld.com/world-news/rest-of-the-world-news/us-newspaper-publishes-15-page-obituary-as-covid-19-cases-rise.html",
      "urlToImage": "https://img.republicworld.com/republic-prod/stories/promolarge/xxhdpi/nojbsc68lge9cgcw_1587383228.jpeg?tr=f-jpeg",
      "publishedAt": "2020-04-20T12:33:00Z",
      "content": "While US President Donald Trump recently claimed that coronavirus outbreak “passed its peak” in the country, an American newspaper published a 15-page obituary of the people who died on April 19. The “heartbreaking” post by a Twitter user has been making seve… [+1956 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Medicaldialogues.in"
      },
      "author": "Hina Zahid",
      "title": "Early family history-based screening of colorectal cancer may lead to better detection - Medical Dialogues",
      "description": "Current guidelines recommend that early screening for colorectal cancer among individuals with a...",
      "url": "https://medicaldialogues.in/oncology/news/early-family-history-based-screening-of-colorectal-cancer-may-lead-to-better-detection-65009",
      "urlToImage": "https://medicaldialogues.in/h-upload/2020/02/03/1200x630_123825-colorectal-cancer-1.jpg?width=1200&height=630",
      "publishedAt": "2020-04-20T12:15:05Z",
      "content": "Current guidelines recommend that early screening for colorectal cancer among individuals with a family history of the disease to identify those at risk of colorectal cancer.\r\nIn an analysis that included information on adults diagnosed with colorectal cancer… [+2422 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Devdiscourse.com"
      },
      "author": "PTI",
      "title": "Global coronavirus toll tops 165,000 - Devdiscourse",
      "description": "The worldwide death toll from the novel coronavirus pandemic rose to 165,216 on Monday, according to a tally from official sources compiled by AFP. More than 2",
      "url": "https://www.devdiscourse.com/article/international/1015803-global-coronavirus-toll-tops-165000",
      "urlToImage": "https://www.devdiscourse.com/remote.axd?https://devdiscourse.blob.core.windows.net/devnews/16_04_2020_17_23_56_1955421.jpg?width=920&format=jpeg",
      "publishedAt": "2020-04-20T12:12:20Z",
      "content": "The worldwide death toll from the novel coronavirus pandemic rose to 165,216 on Monday, according to a tally from official sources compiled by AFP. More than 2,403,410 declared cases have been registered in 193 countries and territories since the epidemic fir… [+1370 chars]"
    },
    {
      "source": {
        "id": "the-times-of-india",
        "name": "The Times of India"
      },
      "author": "PTI",
      "title": "Quarantine health tips: When working remotely, stay hydrated, check caffeine intake & avoid junk - Economic Times",
      "description": "It is extremely essential to complete 8-12 glasses intake of water daily.",
      "url": "https://economictimes.indiatimes.com/magazines/panache/quarantine-health-tips-when-working-remotely-stay-hydrated-check-caffeine-intake-avoid-junk/articleshow/75249134.cms",
      "urlToImage": "https://img.etimg.com/thumb/msid-75249304,width-1070,height-580,imgsize-624679,overlay-etpanache/photo.jpg",
      "publishedAt": "2020-04-20T12:06:12Z",
      "content": "BENGALURU: One of the biggest challenges one faces when working from home during the lockdown period is to keep nutrition in check, says a nutritionist.\r\nNutritionist Pooja Makhija says being hydrated, keeping a check on caffeine consumption, planning meal ti… [+3813 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Theprint.in"
      },
      "author": "Mohana Basu",
      "title": "Kerala hospital begins HCQ clinical trial even after ICMR says no basis for such studies - ThePrint",
      "description": "The trial assumes the ICMR-recommended HCQ regimen is an ‘effective treatment’. However, ICMR chief epidemiologist says there isn’t enough evidence behind this.",
      "url": "https://theprint.in/health/kerala-hospital-begins-hcq-clinical-trial-even-after-icmr-says-no-basis-for-such-studies/405305/",
      "urlToImage": "https://d2c7ipcroan06u.cloudfront.net/wp-content/uploads/2020/04/Untitled-design-48.jpg",
      "publishedAt": "2020-04-20T11:59:13Z",
      "content": "New Delhi: The Indian Council of Medical Research (ICMR) believes there is no basis for a clinical trial to test the efficacy of hydroxychloroquine (HCQ) as a preventive drug to tackle Covid-19. But a hospital in Kerala has begun work on a trial registered wi… [+4831 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Financialexpress.com"
      },
      "author": "FE Online",
      "title": "COVID-19: Top 3 immunity boosting concoctions to enjoy at home - The Financial Express",
      "description": "Here are a few concoction options to dive in and give a twist to your regular routine to enjoy good immunity:",
      "url": "https://www.financialexpress.com/lifestyle/covid-19-top-3-immunity-boosting-concoctions-to-enjoy-at-home/1934196/",
      "urlToImage": "https://images.financialexpress.com/2020/04/immunity-drinks.jpg",
      "publishedAt": "2020-04-20T11:24:40Z",
      "content": "By Nmami Agarwal\r\nCOVID-19: With the sudden wave of fear of coronavirus, all of us have become cautious about our hygiene and our sneezing and coughing behaviour, we should also pay little attention to enhancing our immunity and whats a better way to start fr… [+2778 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Businessinsider.in"
      },
      "author": "Prabhjote Gill",
      "title": "MIT scientists find a way to protect lungs of Coronavirus patients from ‘cytokine storms’ - Business Insider India",
      "description": "A team of researchers from the Massachusetts Institute of Technology (MIT) have developed special proteins to help save the lungs of Coronavirus patients.",
      "url": "https://www.businessinsider.in/science/health/news/mit-scientists-find-a-way-to-protect-lungs-of-coronavirus-patients-from-cytokine-storms/articleshow/75250836.cms",
      "urlToImage": "https://www.businessinsider.in/photo/75250836/mit-scientists-find-a-way-to-protect-lungs-of-coronavirus-patients-from-cytokine-storms.jpg?imgsize=224556",
      "publishedAt": "2020-04-20T11:21:00Z",
      "content": "Just because humans don’t have natural immunity against Coronavirus doesn’t mean that the body doesn’t try to fight back. One of the ways it can do this is by launching a ‘cytokine storm’ — a burst of immune overreaction. \r\nAs the body fights against the viru… [+3347 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Shethepeople.tv"
      },
      "author": "fb.com/anushika.srivastava.10",
      "title": "Testicles Might Be Making Men More Vulnerable To Coronavirus: Study - SheThePeople",
      "description": "A new study found that testes might be responsible for coronavirus in men, making them more vulnerable to catching the COVID-19.",
      "url": "https://www.shethepeople.tv/news/testes-might-be-making-men-vulnerable-coronavirus-study",
      "urlToImage": "https://www.shethepeople.tv/wp-content/uploads/2020/03/6.jpg",
      "publishedAt": "2020-04-20T11:19:40Z",
      "content": "More men are dying of coronavirus than women. Why? A new study shows that the presence of testicles in men makes them more vulnerable to longer and more severe cases COVID-19. The collaborative study was conducted by the Department of Oncology, Cell Biology, … [+3672 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Deccanherald.com"
      },
      "author": "PTI",
      "title": "Coronavirus: Indian-origin pregnant doctor protests against PPE shortage at 10 Downing Street in London - Deccan Herald",
      "description": "A pregnant Indian-origin doctor has staged a protest outside British prime minister's office at 10 Downing Street against the persistent shortage of personal protective equipment, mainly surgical gowns, for the UK's National Health Service medics amid the cor…",
      "url": "https://www.deccanherald.com/international/world-news-politics/coronavirus-indian-origin-pregnant-doctor-protests-against-ppe-shortage-at-10-downing-street-in-london-827688.html",
      "urlToImage": "https://www.deccanherald.com/sites/dh/files/article_images/2020/04/20/Test-1587379429.jpg",
      "publishedAt": "2020-04-20T10:43:49Z",
      "content": "A pregnant Indian-origin doctor has staged a protest outside British prime minister's office at 10 Downing Street against the persistent shortage of personal protective equipment, mainly surgical gowns, for the UK's National Health Service medics amid the cor… [+3734 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Indianexpress.com"
      },
      "author": "Abantika Ghosh",
      "title": "Explained: How pooled testing works, when it helps - The Indian Express",
      "description": "Coronavirus (COVID-19): Last week, the ICMR brought out an advisory on pooled testing, ideally in districts where incidence of COVID-19 is low.",
      "url": "https://indianexpress.com/article/explained/coronavirus-infection-how-pooled-testing-works-when-it-helps-6370001/",
      "urlToImage": "https://images.indianexpress.com/2020/04/pool-testing.jpg?w=759",
      "publishedAt": "2020-04-20T10:38:33Z",
      "content": "Written by Abantika Ghosh\r\n | New Delhi | \r\nUpdated: April 20, 2020 4:04:23 pm\r\nThe ICMR has also set an upper limit of five samples that can be pooled; this is to avoid false negatives because of excessive dilution. More samples can, however, be pooled if it… [+5350 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Republicworld.com"
      },
      "author": "Kunal Gaurav",
      "title": "French Nobel laureate claims coronavirus was made in Wuhan lab - Republic World - Republic World",
      "description": "A Nobel prize-winning scientist has claimed that the novel coronavirus originated from a Wuhan laboratory in an attempt to manufacture a vaccine against HIV.",
      "url": "https://www.republicworld.com/world-news/rest-of-the-world-news/french-nobel-laureate-claims-coronavirus-originated-from-wuhan-lab.html",
      "urlToImage": "https://img.republicworld.com/republic-prod/stories/promolarge/xxhdpi/ywpjdmf4vz9ccbuo_1587376785.jpeg?tr=f-jpeg",
      "publishedAt": "2020-04-20T10:23:00Z",
      "content": "French Nobel prize-winning scientist Luc Montagnier has claimed that the novel coronavirus originated from a Wuhan laboratory while attempting to manufacture a vaccine against HIV (Human Immunodeficiency Virus). During an interview with a French news channel,… [+2291 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Indianewengland.com"
      },
      "author": '',
      "title": "Can binge drinkers be tamed via switching off a brain receptor? - India New England",
      "description": "New York– Binge drinkers, here comes good news. A team of US researchers has found that deactivating a stress-signaling system in a brain area known for motivation and emotion-related behavio…",
      "url": "https://indianewengland.com/2020/04/can-binge-drinkers-be-tamed-via-switching-off-a-brain-receptor/",
      "urlToImage": "https://indianewengland.com/wp-content/uploads/2018/12/Alcohl-iStock.jpg",
      "publishedAt": "2020-04-20T10:07:30Z",
      "content": "New York– Binge drinkers, here comes good news. A team of US researchers has found that deactivating a stress-signaling system in a brain area known for motivation and emotion-related behaviours can decrease binge drinking.\r\nThe US National Institutes of Heal… [+3457 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "News18.com"
      },
      "author": "News18",
      "title": "How to Wash Off Germs from Vegetables and Perishables During Coronavirus - News18",
      "description": "In attempts of cleaning the grocery, do not clean it with soap water or disinfectant which are used on hard surfaces like doorknobs, grills or calling bells.",
      "url": "https://www.news18.com/news/buzz/how-to-wash-off-germs-from-vegetables-and-perishables-during-coronavirus-2585067.html",
      "urlToImage": "https://images.news18.com/ibnlive/uploads/2020/04/1587376223_untitled-design-5.png",
      "publishedAt": "2020-04-20T09:54:33Z",
      "content": "While everyone is staying indoors to contain the spread of coronavirus, stepping out to buy essential commodities, seek medical help and venturing outside for other necessary activities is unavoidable. But we can minimize risk by wearing masks and washing han… [+1895 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Firstpost.com"
      },
      "author": '',
      "title": "Coronavirus Outbreak: Why are more men dying from COVID-19 infections than women? - Firstpost",
      "description": "Sex differences in the frequency, severity and treatment efficacy for many diseases, not just COVID-19, were pointed out long ago.",
      "url": "https://www.firstpost.com/health/coronavirus-outbreak-why-are-more-men-dying-from-covid-19-infections-than-women-8278481.html",
      "urlToImage": "https://images.firstpost.com/wp-content/uploads/2020/04/file-20200417-192698-16ktxpz-1.jpg",
      "publishedAt": "2020-04-20T09:33:18Z",
      "content": ''
    },
    {
      "source": {
        "id": '',
        "name": "Dailyexcelsior.com"
      },
      "author": "https://www.facebook.com/dailyexcelsior",
      "title": "Hrithik, Ajay, Varun urge those recovered from COVID-19 to donate blood to fight virus - Daily Excelsior",
      "description": "Mumbai: Actors Hrithik Roshan, Ajay Devgn and Varun Dhawan appealed to people who have recovered from coronavirus to donate blood to help those in",
      "url": "https://www.dailyexcelsior.com/hrithik-ajay-varun-urge-those-recovered-from-covid-19-to-donate-blood-to-fight-virus/",
      "urlToImage": "https://www.dailyexcelsior.com/wp-content/uploads/2016/12/hrithik-roshan-759.jpg",
      "publishedAt": "2020-04-20T07:41:00Z",
      "content": "Mumbai: Actors Hrithik Roshan, Ajay Devgn and Varun Dhawan appealed to people who have recovered from coronavirus to donate blood to help those in critical condition.The local municipal body, Brihanmumbai Municipal Corporation (BMC) said that recovered COVID-… [+1116 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Youtube.com"
      },
      "author": '',
      "title": "HEALTH FOCUS: Impact of COVID-19 on the Universal health coverage - NTVUganda",
      "description": "Around the world, the COVID-19 pandemic is having a huge impact on health systems, economies and the lives, livelihoods and wellbeing of people and communiti...",
      "url": "https://www.youtube.com/watch?v=pvAnEiZ2Prk",
      "urlToImage": "https://i.ytimg.com/vi/pvAnEiZ2Prk/maxresdefault.jpg",
      "publishedAt": "2020-04-20T06:44:49Z",
      "content": ''
    },
    {
      "source": {
        "id": '',
        "name": "Medicaldialogues.in"
      },
      "author": "Medical Dialogues Bureau",
      "title": "Doctor stranded in India lockdown flies back to work at UK hospital - Medical Dialogues",
      "description": "London - An Indian-origin doctor who had been stranded in Delhi amid Indias ongoing coronavirus...",
      "url": "https://medicaldialogues.in/news/health/doctors/doctor-stranded-in-india-lockdown-flies-back-to-work-at-uk-hospital-64999",
      "urlToImage": "https://medicaldialogues.in/h-upload/2020/04/09/1200x630_126914-doctors.jpg?width=1200&height=630",
      "publishedAt": "2020-04-20T04:30:45Z",
      "content": "London - An Indian-origin doctor who had been stranded in Delhi amid India's ongoing coronavirus lockdown on Friday expressed his relief at being back at work at his hospital in Suffolk, eastern England. \r\n Dr Sushil Misra, a consultant in acute medicine for … [+3440 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Sciencealert.com"
      },
      "author": "Amelie Bottollier-Depois, AFP",
      "title": "Scientists Still Don't Know if Recovering From COVID-19 Confers Immunity or Not - ScienceAlert",
      "description": "Even as virologists zero in on the virus that causes COVID-19, a very basic question remains unanswered: do those who recover from the disease have immunity?",
      "url": "https://www.sciencealert.com/scientists-still-don-t-know-if-recovering-from-covid-19-confers-immunity-or-not",
      "urlToImage": "https://www.sciencealert.com/images/2020-04/processed/DontKnowIfRecoveringConveysImmunity_1024.jpg",
      "publishedAt": "2020-04-20T01:43:13Z",
      "content": "Even as virologists zero in on the virus that causes COVID-19, a very basic question remains unanswered: do those who recover from the disease have immunity?\r\nThere is no clear answer to this question, experts say, even if many have assumed that contracting t… [+5516 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Youtube.com"
      },
      "author": '',
      "title": "Children in COVID-19 pandemic - Times of Oman",
      "description": "Children in COVID-19 pandemic The belief that the children will not be infected with COVID-19 is untrue, given that a number of children have been infected i...",
      "url": "https://www.youtube.com/watch?v=m31py7PxvCI",
      "urlToImage": "https://i.ytimg.com/vi/m31py7PxvCI/maxresdefault.jpg",
      "publishedAt": "2020-04-20T01:00:07Z",
      "content": ''
    },
    {
      "source": {
        "id": '',
        "name": "Bbc.com"
      },
      "author": "https://www.facebook.com/bbcnews",
      "title": "Coronavirus: University's rapid test could be used 'in weeks' - BBC News",
      "description": "A portable device capable of an accurate result within 30 minutes has also been developed.",
      "url": "https://www.bbc.com/news/uk-wales-52347827",
      "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/E3A1/production/_111837285_coronavirustest.jpg",
      "publishedAt": "2020-04-19T23:44:08Z",
      "content": "Image copyrightSamara Heisz/Getty ImagesImage caption\r\n The university's test uses different chemicals to the current accredited test, allowing them to avoid bottlenecks in the supply chain\r\nA rapid test for detecting Covid-19 has been developed by scientists… [+3367 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Nzherald.co.nz"
      },
      "author": "Rowan Quinn",
      "title": "Covid 19 coronavirus: Up to 30000 surgeries called off during lockdown - New Zealand Herald",
      "description": "Only the most urgent procedures carried out as elective surgeries put on hold.",
      "url": "https://www.nzherald.co.nz/nz/news/article.cfm?c_id=1&objectid=12325949",
      "urlToImage": "https://www.nzherald.co.nz/resizer/x6f7-GPzFnnMm1d7cx0AKVbYiU0=/1200x0/smart/filters:quality(70)/arc-anglerfish-syd-prod-nzme.s3.amazonaws.com/public/TFZUMDS675BSPIPXVQLT66UB5E.jpg",
      "publishedAt": "2020-04-19T19:37:35Z",
      "content": "From RNZ\r\n Hospitals deferred thousands of operations as they prepared for a possible wave of Covid-19 cases - and to minimise contact under alert level 4.\r\n The most urgent surgeries were still being done under the lockdown but elective surgery had largely b… [+2336 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Dailypioneer.com"
      },
      "author": "The Pioneer",
      "title": "The hunt for a vaccine - Daily Pioneer",
      "description": "Our scientists are working on a multi-purpose antidote. This highlights the need to fund R&amp;D in a post-COVID world\n\nAs ever-increasing numbers of people test positive for Coronavirus daily, Indian scientists, medical professionals and researchers are toil…",
      "url": "https://www.dailypioneer.com/2020/columnists/the-hunt-for-a-vaccine.html",
      "urlToImage": "https://www.dailypioneer.com/uploads/2020/story/images/big/the-hunt-for-a-vaccine-2020-04-20.jpg",
      "publishedAt": "2020-04-19T18:31:42Z",
      "content": "Our scientists are working on a multi-purpose antidote. This highlights the need to fund R&amp;D in a post-COVID world\r\nAs ever-increasing numbers of people test positive for Coronavirus daily, Indian scientists, medical professionals and researchers are toil… [+2888 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Hindustantimes.com"
      },
      "author": "Mehul Thakkar",
      "title": "BMC to put high-risk contacts on anti-malarial drug - Hindustan Times",
      "description": "",
      "url": "https://www.hindustantimes.com/mumbai-news/bmc-to-put-high-risk-contacts-on-anti-malarial-drug/story-Ao6SlpXcIk7rfqqmUImUMJ.html",
      "urlToImage": "https://www.hindustantimes.com/images/app-images/2019/7/960x540.jpg",
      "publishedAt": "2020-04-19T17:58:33Z",
      "content": "The Brihanmumbai Municipal Corporation (BMC) on Sunday announced its decision to treat high-risk contacts of Covid-19 patients, with doses of hydroxychloroquine (HCQ), an anti-malarial drug.\r\nHydroxychloroquine is an anti-malarial drug being used to prevent t… [+1490 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Financialexpress.com"
      },
      "author": "FE Online",
      "title": "Israeli scientist granted US patent for coronavirus vaccine design - The Financial Express",
      "description": "The vaccine is proposed by Professor Jonathan Gershoni of the School of Molecular Cell Biology and Biotechnology at the university's George S. Wise Faculty of Life Sciences.",
      "url": "https://www.financialexpress.com/lifestyle/health/israeli-scientist-granted-us-patent-for-novel-coronavirus-vaccine-design/1933540/",
      "urlToImage": "https://images.financialexpress.com/2020/04/covid660-5.jpg",
      "publishedAt": "2020-04-19T17:17:08Z",
      "content": "In a major breakthrough, an Israeli scientist at the Tel Aviv University has been granted a US patent for his innovative vaccine design for the corona family of viruses, a press statement by the varsity said on Sunday.The patent has been granted by the United… [+1961 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Youtube.com"
      },
      "author": '',
      "title": "\"This is not uncommon\": How the coronavirus leapt from bats to humans - Democracy Now!",
      "description": "As President Trump endorses a fringe conspiracy theory suggesting that the novel coronavirus originated in a Chinese lab, zoologist and disease ecologist Pet...",
      "url": "https://www.youtube.com/watch?v=dA3oV3vTwmo",
      "urlToImage": "https://i.ytimg.com/vi/dA3oV3vTwmo/maxresdefault.jpg",
      "publishedAt": "2020-04-19T15:30:03Z",
      "content": ''
    },
    {
      "source": {
        "id": "the-times-of-india",
        "name": "The Times of India"
      },
      "author": "PTI",
      "title": "99 institutes willing to take part in clinical trial of plasma therapy for COVID-19 treatment: ICMR - Economic Times",
      "description": "Convalescent plasma is an experimental procedure for COVID-19 patients. As per the guidelines, hospitals and institutions planning to provide this modality of treatment should do so in a clinical trial with protocols which are cleared by the Institutional Eth…",
      "url": "https://economictimes.indiatimes.com/news/politics-and-nation/99-institutes-willing-to-take-part-in-clinical-trial-of-plasma-therapy-for-covid-19-treatment-icmr/articleshow/75236910.cms",
      "urlToImage": "https://img.etimg.com/thumb/msid-75237025,width-1070,height-580,imgsize-542487,overlay-economictimes/photo.jpg",
      "publishedAt": "2020-04-19T15:25:05Z",
      "content": "NEW DELHI: The Indian Council of Medical Research (ICMR) has received 99 applications from institutes expressing interest in participating in a randomised controlled study to assess the safety and efficacy of convalescent plasma to limit complications associa… [+2066 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Businessinsider.in"
      },
      "author": "Julian Kossoff",
      "title": "Medical detection dogs able to sniff 750 people an hour could help identify coronavirus cases, researchers say - Business Insider India",
      "description": "Scientists in the UK believe that medical detection dogs could be able to help identify coronavirus cases in humans. Medical detection dogs are already being",
      "url": "https://www.businessinsider.in/science/news/medical-detection-dogs-able-to-sniff-750-people-an-hour-could-help-identify-coronavirus-cases-researchers-say/articleshow/75237387.cms",
      "urlToImage": "https://www.businessinsider.in/photo/75237387/medical-detection-dogs-able-to-sniff-750-people-an-hour-could-help-identify-coronavirus-cases-researchers-say.jpg?imgsize=196062",
      "publishedAt": "2020-04-19T15:01:00Z",
      "content": "Specially trained medical detection dogs could be the solution to the crisis in the lack of testing that many countries are facing during the coronavirus pandemic.\r\nThe dogs are capable of sniff testing 750 people an hour, according to the head of a non-profi… [+1936 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Scoopwhoop.com"
      },
      "author": "Dhirendra Kumar",
      "title": "10 DIY Skincare Hacks That Will Help You Get Rid Of Acne - ScoopWhoop",
      "description": "Go Acne Go!",
      "url": "https://www.scoopwhoop.com/health/10-diy-skin-hacks-that-will-help-you-get-rid-of-acne/",
      "urlToImage": "https://s4.scoopwhoop.com/anj2/5e9bf95b18ac8111b319cd90/a26a343b-2a82-4169-bd99-860a945b80a3.jpg",
      "publishedAt": "2020-04-19T14:26:54Z",
      "content": "Do you struggle with acne scars? Acne is normally caused by hormonal changes as a teenager, but it can last much longer. It is one of the most common skin conditions in the world, affecting an estimated 85% of people at some point in their lives. \r\nIf you dis… [+4350 chars]"
    },
    {
      "source": {
        "id": "reuters",
        "name": "Reuters"
      },
      "author": "Reuters Editorial",
      "title": "Swiss coronavirus death toll rises to 1,135, confirmed infections hit 27,740 - Reuters India",
      "description": "The Swiss death toll from the novel coronavirus has reached 1,135 people, the country's public health agency said on Sunday, rising from 1,111 on Saturday.",
      "url": "https://in.reuters.com/article/us-health-coronavirus-swiss-idINKBN2210FO",
      "urlToImage": "https://s3.reutersmedia.net/resources/r/?m=02&d=20200419&t=2&i=1515637445&w=1200&r=LYNXMPEG3I08J",
      "publishedAt": "2020-04-19T11:23:00Z",
      "content": "ZURICH (Reuters) - The Swiss death toll from the novel coronavirus has reached 1,135 people, the country’s public health agency said on Sunday, rising from 1,111 on Saturday. \r\nThe number of people showing positive tests for the disease increased to 27,740, i… [+81 chars]"
    },
    {
      "source": {
        "id": '',
        "name": "Indiatvnews.com"
      },
      "author": "India TV Video Desk",
      "title": "1,334 fresh COVID-19 cases reported since Saturday, 27 deaths in last 24 hours: Health Ministry - India TV",
      "description": "1334 new COVID19 cases & 27 deaths have been reported in last 24 hours, taking total cases to 15712 & deaths to 507 in India: Health Ministry",
      "url": "https://www.indiatvnews.com/video/news/1-334-fresh-covid-19-cases-reported-since-saturday-27-deaths-in-last-24-hours-health-ministry-609196",
      "urlToImage": "https://thumbs.indiatvnews.com/vod/0_748s8mhx_big_thumb.jpg",
      "publishedAt": "2020-04-19T11:04:48Z",
      "content": "Do kapalbhati, anulom vilom to cure lipoma: Swami Ramdev"
    },
    {
      "source": {
        "id": '',
        "name": "Tweaktown.com"
      },
      "author": "Anthony Garreffa",
      "title": "These dogs can sniff 750 people per hour to screen for coronavirus - TweakTown",
      "description": "Dogs get samples of clothes worn by coronavirus patients, trained to sniff-and-detect coronavirus COVID-19",
      "url": "https://www.tweaktown.com/news/71890/these-dogs-can-sniff-750-people-per-hour-to-screen-for-coronavirus/index.html",
      "urlToImage": "https://images.tweaktown.com/news/7/1/71890_07_these-dogs-can-sniff-750-people-per-hour-to-screen-for-coronavirus_full.jpg",
      "publishedAt": "2020-04-19T09:20:03Z",
      "content": "COVID-19 coronavirus detection might be getting easier, with a new project in the works that is training dogs to sniff out coronavirus.\r\nThe new project is the only one in the world training dogs to sniff out coronavirus, with the Medical Detection Dogs chari… [+1912 chars]"
    }
  ]
    return render_template('index.html', lists = lists)

app.run(debug = True)