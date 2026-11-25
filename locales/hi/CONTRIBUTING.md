# योगदान मार्गदर्िका

नए प्रोजेक्ट, पेपर और प्रमाण-सुधार का स्वागत है। कम star अस्वीकृति का कारण नहीं है।

1. प्रविष्टि `data/projects.json` या `data/papers.json` में जोड़ें; जनरेटेड README तालिकाएँ सीधे न बदलें।
2. canonical GitHub पता या पेपर का मूल पृष्ठ दें, कम-से-कम एक ऐसा स्रोत जो वर्णित तंत्र को सिद्ध करे, और सत्यापन-तिथि।
3. बताएँ कि यह पूर्ण असिस्टेंट है, एक्सटेंशन, Harness, कंट्रोल घटक या रिसर्च कोड; ट्रिगर विधि विशिष्ट होनी चाहिए। अपुष्ट क्षमता पर "असत्यापित" लिखें; roadmap कोImplemented फ़ीचर न बताएँ।
4. लाइसेंस जाँचें। पूर्ण लाइसेंस-पाठ न मिले तो पहले उम्मीदवार/रिसर्च प्रविष्टि के रूप में रखें; ग़ैर-व्यावसायिक प्रतिबंध वाले सोर्स-कोड को सत्यापित खुले लाइसेंस न बताएँ।
5. नाम बदलने पर GitHub canonical repo के अनुसार अपडेट करें; एक ही पेपर को arXiv ID से de-duplicate करें, पुराने नाम नोट में रखे जा सकते हैं।
6. नीचे की कमांड चलाएँ और जनरेटेड परिणाम कमिट करें। नए रिपॉज़िटरी के लिए पूर्ण मीट्रिक स्नैपशॉट दोबारा लें।

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests
python scripts/build.py --check
```

फ़ंक्शन-विवरण अपडेट करते समय प्रमाण-commit SHA फिक्स करें; स्वचालित star अपडेट से पुराने फ़ंक्शन-निर्णयों को "अभी सत्यापित" न बता दिया जाए। वर्गीकरण विधि `docs/taxonomy.md` में, रैंकिंग विधि `docs/methodology.md` में है।

इस रिपॉज़िटरी में निजी खोज-सेवा पते, टोकन, आंतरिक लेख-पाठ, हस्ताक्षरित डाउनलोड लिंक या व्यक्तिगत डेटा प्रकाशित करना निषिद्ध।

## बहुभाषी फ़ाइलें

- `data/projects.json` चीनी में मानक समीक्षा-डेटा है: तथ्य यहीं एक बार बदलते हैं।
- अन्य भाषाओं का पाठ `locales/<lang>/entries.json` (`description`, `trigger`, `boundary`, `license_label`, `license_note`) और `locales/<lang>/ui.json` से आता है; शोध-पत्रों का पाठ `locales/<lang>/papers.json` (`title`, `summary`, `boundary`, `publication_note`) से आता है; `zh` सीधे `data/projects.json` और `data/papers.json` पर गिरता है, इसलिए `locales/zh/entries.json` नहीं है।
- नया प्रोजेक्ट जोड़ते समय या स्थिति, सीमा और लाइसेंस-निष्कर्ष बदलते समय उसी PR में en/es/hi/fr चारों locale पूरी करें, वरना `python scripts/build.py --check` और `python -m unittest discover -s tests -v` फेल होंगे।
- स्थैतिक डॉक्यूमेंटेशन: अंग्रेज़ी रूट `docs/` और `CONTRIBUTING.md` में, अन्य भाषाएँ `locales/<lang>/` के समान सापेक्ष पथों पर। mirror में सापेक्ष लिंक फ़ाइल की अपनी डायरेक्टरी से रिज़ॉल्व होते हैं; रूट के `data/`, `scripts/`, `research/`, `LICENSE`, `record/` की ओर लिंक `../../` जैसे हैं, `docs/` के अंदर से `../../../`। `docs/readme-intro.md` अपवाद है: यह README में जोड़ा जाता है और भाषा-मूल से रिज़ॉल्व होता है।
- `record/` और `research/` लिखे जाने समय के मूल पाठ रखते हैं, ऑडिट-ट्रेस के लिए; इन्हें मशीन-अनुवादित नहीं किया जाता।
- जनरेटेड फ़ाइलें (`README.md`, `docs/projects.md`, `docs/rankings.md`, `data/rankings.csv`, हर भाषा के mirror की समान-नाम फ़ाइलें) हाथ से न बदलें; `python scripts/build.py` इन्हें बनाता है।
