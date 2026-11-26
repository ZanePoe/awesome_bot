# प्रोजेक्ट विवरण और प्रमाण

हर फ़ंक्शन सार्वजनिक डॉक्यूमेंटेशन से सत्यापित है; इन्हें इंस्टॉल करके चलाया या समग्र क्षमता-परीक्षण पूरा नहीं किया गया। प्रमाण सत्यापन के समय के commit पर फिक्स रहते हैं; बाद में मीट्रिक रीफ़्रेश होने से फ़ंक्शन के निर्णय स्वतः नहीं बदलते।


<a id="openclaw--openclaw"></a>

## [OpenClaw](https://github.com/openclaw/openclaw)

चैनल मैसेजिंग, स्मृति और टूल्स से जुड़ा सदैव-चालू व्यक्तिगत असिस्टेंट।

- श्रेणी: सदैव-चालू व्यक्तिगत असिस्टेंट और हल्के रनटाइम; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: शेड्यूल / heartbeat / इवेंट।
- सीमा: बैकग्राउंड निष्पादन gateway पर निर्भर; हर प्लेटफ़ॉर्म और टूल की अनुमतियाँ अलग से कॉन्फ़िगर करनी होती हैं।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 11646 कमिट, 90 दिन में 48572 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/openclaw/openclaw/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/openclaw/openclaw/blob/8cb658e39b6dbe1bbe03746bf2a468a898c15da2/README.md#L18) · [स्रोत2](https://docs.openclaw.ai/gateway/heartbeat) · [स्रोत3](https://docs.openclaw.ai/gateway/heartbeat)।

<a id="nousresearch--hermes-agent"></a>

## [Hermes Agent](https://github.com/NousResearch/hermes-agent)

दीर्घकालिक स्मृति, स्किल संचय और क्रॉस-चैनल शेड्यूल डिलीवरी वाला पर्सनल Agent।

- श्रेणी: सदैव-चालू व्यक्तिगत असिस्टेंट और हल्के रनटाइम; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: शेड्यूल / सेशन heartbeat।
- सीमा: फ़ंक्शन आधिकारिक डॉक्यूमेंटेशन पर आधारित; इस निर्देशिका में इन्हें चलाकर टेस्ट नहीं किया गया।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 17323 कमिट, 90 दिन में 50744 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/NousResearch/hermes-agent/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/NousResearch/hermes-agent/blob/cad0aaaf0d77ffa4899ebf0d3db8bae7a6b5147f/README.md#L27)।

<a id="hkuds--nanobot"></a>

## [nanobot](https://github.com/HKUDS/nanobot)

हल्का Python पर्सनल Agent, जिसमें फ़ाइलें, स्मृति, MCP और दीर्घकालिक लक्ष्य शामिल हैं।

- श्रेणी: सदैव-चालू व्यक्तिगत असिस्टेंट और हल्के रनटाइम; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: शेड्यूल / लोकल ट्रिगर।
- सीमा: बैकग्राउंड सेवा रीस्टार्ट के बाद छूटी हुई शेड्यूल टास्क दोबारा नहीं चलाती; आधिकारिक रीकवरी नोट देखें।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 311 कमिट, 90 दिन में 1220 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/HKUDS/nanobot/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/HKUDS/nanobot/blob/ce3aa50e70f6550d7be19f73f2cfa2ba6fb66880/README.md#L63)।

<a id="zeroclaw-labs--zeroclaw"></a>

## [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw)

Rust Agent रनटाइम, जिसमें बैकग्राउंड सेवा, टूल्स और इवेंट-ट्रिगर्ड फ़्लो हैं।

- श्रेणी: सदैव-चालू व्यक्तिगत असिस्टेंट और हल्के रनटाइम; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: cron / webhook / MQTT।
- सीमा: कंप्यूटर-संचालन का दायरा कॉन्फ़िगर किए गए टूल्स और निष्पादन वातावरण पर निर्भर है।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 293 कमिट, 90 दिन में 1073 कमिट।
- लाइसेंस: [Apache-2.0](https://api.github.com/repos/zeroclaw-labs/zeroclaw/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/zeroclaw-labs/zeroclaw/blob/683d10139bc200ab8db768fcb4515f79404846ac/README.md#L83)।

<a id="milind-soni--openmausbot"></a>

## [OpenMausBot](https://github.com/milind-soni/OpenMausBot)

लोकल-फ़र्स्ट मल्टी-Bot चैट ऐप, जिसमें हर Bot के अपने मॉडल, थ्रेड स्मृति, कंप्यूटर और जुड़े ऐप हो सकते हैं।

- श्रेणी: सदैव-चालू व्यक्तिगत असिस्टेंट और हल्के रनटाइम; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: schedules / webhooks / app events।
- सीमा: Bot चलाने के लिए मशीन पर Claude, Codex, Grok आदि CLI या संगत मॉडल प्रदाता चाहिए; क्लाउड डेस्कटॉप, Composio और enterprise फ़ीचर की सेवा/लाइसेंस सीमा अलग है।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 6899 कमिट, 90 दिन में 12973 कमिट।
- लाइसेंस: [Apache-2.0 (enterprise/ छोड़कर)](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L519); enterprise/ हटाने पर Apache-2.0 ओपन-सोर्स संस्करण; enterprise/ अलग source-available लाइसेंस है, प्रोडक्शन में चालू करने के लिए लाइसेंस की ज़रूरत है और पुनर्वितरण या थर्ड-पार्टी होस्टिंग निषिद्ध।
- फ़ंक्शन सत्यापन: 2026-11-06; [स्रोत1](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L73) · [स्रोत2](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L413) · [स्रोत3](https://github.com/milind-soni/OpenMausBot/blob/083fd7b51405e6d0c01e189b2f65ab0322509b5a/README.md#L519)।

<a id="nanocoai--nanoclaw"></a>

## [NanoClaw](https://github.com/nanocoai/nanoclaw)

मैसेज चैनल से संचालित असिस्टेंट, जो एजेंट को कंटेनर में चलाता और आवधिक कार्य निभाता है।

- श्रेणी: सदैव-चालू व्यक्तिगत असिस्टेंट और हल्के रनटाइम; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: शेड्यूल / script gates।
- सीमा: कार्यान्वयन वातावरण कंटेनर है; इससे किसी भी होस्ट डेस्कटॉप को संचालित करने का दावा नहीं किया जा सकता।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 152 कमिट, 90 दिन में 525 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/nanocoai/nanoclaw/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/nanocoai/nanoclaw/blob/f7440e85f8b2a75b17fc9a08f0cc6aacf723a1e2/README.md#L65)।

<a id="elie222--rakazo"></a>

## [Rakazo](https://github.com/elie222/rakazo)

स्व-चयनित मॉडल और सैंडबॉक्स के साथ सेल्फ-होस्ट होने वाला निरंतर Bot और टीम कंप्यूटर वर्कस्पेस।

- श्रेणी: सदैव-चालू व्यक्तिगत असिस्टेंट और हल्के रनटाइम; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: routines।
- सीमा: निजी कंप्यूटर, टीम कंप्यूटर और कंटेनर की क्षमताएँ कॉन्फ़िगरेशन से अलग होती हैं।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 3063 कमिट, 90 दिन में 4666 कमिट।
- लाइसेंस: [Apache-2.0](https://api.github.com/repos/elie222/rakazo/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/elie222/rakazo/blob/ed67158935a95b6153aad6c9cd874c6cc8d2413d/README.md#L24)।

<a id="nano-muse--nanomuse"></a>

## [nanoMuse](https://github.com/nano-muse/nanoMuse)

फ़ोन और कंप्यूटर पर चलता पर्सनल Agent, जो स्मृति, बैकग्राउंड लक्ष्य और डिवाइस संचालन को जोड़ता है।

- श्रेणी: सदैव-चालू व्यक्तिगत असिस्टेंट और हल्के रनटाइम; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: लक्ष्य निरीक्षण / routines।
- सीमा: डिवाइस क्षमताएँ और बैकग्राउंड संचालन की शर्तें प्लेटफ़ॉर्म के हिसाब से अलग हैं; पेपर और सॉफ़्टवेयर में एक-एक प्रविष्टि है।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 846 कमिट, 90 दिन में 2767 कमिट।
- लाइसेंस: [GPL-3.0](https://api.github.com/repos/nano-muse/nanoMuse/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/nano-muse/nanoMuse/blob/57f5c5abed2d66fa19ab8fc39fd52eb365e4f14d/README.md#L80)।

<a id="moltis-org--moltis"></a>

## [Moltis](https://github.com/moltis-org/moltis)

स्मृति, वॉइस, मैसेजिंग, ब्राउज़र और शेड्यूलिंग को जोड़ने वाली व्यक्तिगत Agent सेवा।

- श्रेणी: सदैव-चालू व्यक्तिगत असिस्टेंट और हल्के रनटाइम; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: cron।
- सीमा: मॉडल और आवश्यक इंटीग्रेशन खुद कॉन्फ़िगर करने पड़ते हैं।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 0 कमिट, 90 दिन में 49 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/moltis-org/moltis/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/moltis-org/moltis/blob/8a12400dc10551dfb9a6b568414b91a343ef2d5d/README.md#L28)।

<a id="nearai--ironclaw"></a>

## [IronClaw](https://github.com/nearai/ironclaw)

Rust व्यक्तिगत असिस्टेंट, जो routines और heartbeat से बैकग्राउंड कार्य चलाता है।

- श्रेणी: सदैव-चालू व्यक्तिगत असिस्टेंट और हल्के रनटाइम; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: शेड्यूल / इवेंट / heartbeat।
- सीमा: टूल पृथक्करण एक डिज़ाइन-फ़ीचर है; इसका अर्थ यह नहीं कि इस निर्देशिका ने सुरक्षा का ऑडिट किया है।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 0 कमिट, 90 दिन में 44 कमिट।
- लाइसेंस: [Apache-2.0](https://api.github.com/repos/nearai/ironclaw/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/README.md#L95)।

<a id="afk-surf--comma"></a>

## [Comma](https://github.com/AFK-surf/Comma)

निरंतर टास्क स्थिति और क्रॉस-डिवाइस कार्य को मिलाता है; मॉनिटरिंग लूप से Agent को जगाता है।

- श्रेणी: सदैव-चालू व्यक्तिगत असिस्टेंट और हल्के रनटाइम; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: routines / event loops।
- सीमा: क्लाउड रनटाइम और लोकल डिवाइस कनेक्शन दो अलग घटक हैं।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 2 कमिट, 90 दिन में 10 कमिट।
- लाइसेंस: [AGPL-3.0](https://api.github.com/repos/AFK-surf/Comma/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/AFK-surf/Comma/blob/66ab3dc92475005aea9afd123df36a28e4ef86ab/README.md#L64)।

<a id="sipeed--picoclaw"></a>

## [PicoClaw](https://github.com/sipeed/picoclaw)

कम-संसाधन डिवाइस के लिए Go में बना व्यक्तिगत असिस्टेंट, जिसमें फ़ाइल, निष्पादन और शेड्यूलिंग टूल्स हैं।

- श्रेणी: सदैव-चालू व्यक्तिगत असिस्टेंट और हल्के रनटाइम; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: शेड्यूल।
- सीमा: कम-संसाधन रनटाइम का अर्थ यह नहीं कि बुलाए गए मॉडल या ब्राउज़र भी कम-खर्चीले हों।
- वर्तमान मेंटेनेंस स्थिति: 91–365 दिन बिना कमिट; 30 दिन में 0 कमिट, 90 दिन में 0 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/sipeed/picoclaw/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/sipeed/picoclaw/blob/bbf6893ca7afad27f1d00a0f5a45982a549c6ed6/README.md#L632)।

<a id="khoj-ai--khoj"></a>

## [Khoj](https://github.com/khoj-ai/khoj)

व्यक्तिगत ज्ञान असिस्टेंट, जिसमें डॉक्युमेंट और वेब रिसर्च तथा शेड्यूल ऑटोमेशन है।

- श्रेणी: सदैव-चालू व्यक्तिगत असिस्टेंट और हल्के रनटाइम; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: scheduled automations।
- सीमा: मुख्य रूप से ज्ञान/सूचना कार्य; यह सार्वभौमिक डेस्कटॉप कंट्रोलर नहीं है।
- वर्तमान मेंटेनेंस स्थिति: 91–365 दिन बिना कमिट; 30 दिन में 0 कमिट, 90 दिन में 0 कमिट।
- लाइसेंस: [AGPL-3.0](https://api.github.com/repos/khoj-ai/khoj/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/khoj-ai/khoj/blob/ae229ca894c0b80ad84664afcfdde523b5e87057/README.md#L50) · [स्रोत2](https://docs.khoj.dev/features/automations) · [स्रोत3](https://docs.khoj.dev/features/automations)।

<a id="mikeyobrien--rho"></a>

## [rho](https://github.com/mikeyobrien/rho)

Pi पर आधारित सदैव-चालू व्यक्तिगत संचालन असिस्टेंट, जिसमें स्थायी स्मृति और आवधिक प्रैएक्टिव जाँच है।

- श्रेणी: सदैव-चालू व्यक्तिगत असिस्टेंट और हल्के रनटाइम; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: heartbeat।
- सीमा: यह Pi का ऊपरी-स्तरीय ऐप है; Android और डेस्कटॉप पर संचालन अलग है।
- वर्तमान मेंटेनेंस स्थिति: 91–365 दिन बिना कमिट; 30 दिन में 0 कमिट, 90 दिन में 0 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/mikeyobrien/rho/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/mikeyobrien/rho/blob/073a3ee8a5dc0efd5dd32d773a760575ed38abc7/README.md#L34)।

<a id="maikunari--mame"></a>

## [Mame](https://github.com/maikunari/mame)

स्थायी स्मृति और मैसेज चैनल वाला हल्का सदैव-चालू असिस्टेंट, जो कोडिंग Agent को ऑर्केस्ट्रेट कर सकता है।

- श्रेणी: सदैव-चालू व्यक्तिगत असिस्टेंट और हल्के रनटाइम; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: cron / heartbeat।
- सीमा: छोटे इम्प्लीमेंटेशन के संदर्भ के लिए उपयुक्त; मेंटेनेंस स्कोर परिपक्वता को नहीं दर्शाता।
- वर्तमान मेंटेनेंस स्थिति: 91–365 दिन बिना कमिट; 30 दिन में 0 कमिट, 90 दिन में 0 कमिट।
- लाइसेंस: [README में MIT घोषित](https://github.com/maikunari/mame/blob/20901dd3cbdf3da11e3edcf2c8b4a8ff3b47134c/README.md); लाइसेंस का पूरा पाठ नहीं मिला; उम्मीदवार के रूप में, ओपन-सोर्स अनुशंसा सूची में नहीं।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/maikunari/mame/blob/20901dd3cbdf3da11e3edcf2c8b4a8ff3b47134c/README.md#L300)।

<a id="copilotkit--openbot"></a>

## [OpenBot](https://github.com/CopilotKit/OpenBot)

AG-UI Agent को अलग ब्राउज़र, फ़ाइल वर्कस्पेस, टूल अनुमतियाँ, ऑडिट लॉग और शेड्यूल टास्क देने वाला सेल्फ-होस्ट AI coworker प्लेटफ़ॉर्म।

- श्रेणी: वर्कस्पेस और कंटेक्स्ट असिस्टेंट; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: शेड्यूल routines / मैन्युअल आरंभ।
- सीमा: OpenBot कंप्यूटर वातावरण, नीति, ऑडिट और शेड्यूलिंग संभालता है; Agent क्षमता जुड़े AG-UI endpoint से आती है, और निरंतर सेशन व स्मृति CopilotKit Intelligence पर निर्भर।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 1044 कमिट, 90 दिन में 1449 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/CopilotKit/OpenBot/license); GitHub licenseInfo ने पहचाना; CopilotKit Intelligence की तैनाती और लाइसेंस शर्तें अलग गिनी जाएँगी।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/CopilotKit/OpenBot/blob/5b94b6aa881fb7829abd4c931489415c28815122/README.md#L251) · [स्रोत2](https://github.com/CopilotKit/OpenBot/blob/5b94b6aa881fb7829abd4c931489415c28815122/README.md#L52)।

<a id="agent0ai--agent-zero"></a>

## [Agent Zero](https://github.com/agent0ai/agent-zero)

कंप्यूटर निष्पादन वातावरण में टूल्स, परियोजनाएँ और आवधिक मॉनिटरिंग कार्य चलाने वाला Agent।

- श्रेणी: वर्कस्पेस और कंटेक्स्ट असिस्टेंट; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: scheduled operations।
- सीमा: सीमा कॉन्फ़िगर किए गए निष्पादन वातावरण तक; डिफ़ॉल्ट रूप से होस्ट के सभी संसाधन पर नियंत्रण नहीं।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 108 कमिट, 90 दिन में 438 कमिट।
- लाइसेंस: [MIT](https://github.com/agent0ai/agent-zero/blob/ba9b67df0f54ac78106ae85c552ef5d2458f7c9a/LICENSE); रूट LICENSE का मानवीय सत्यापन।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/agent0ai/agent-zero/blob/ba9b67df0f54ac78106ae85c552ef5d2458f7c9a/README.md#L259)।

<a id="anil-matcha--suparagent"></a>

## [Suparagent](https://github.com/Anil-matcha/suparagent)

नाम दिए गए AI coworkers, टीम डेलीगेशन, बातचीत, स्मृति, routines, टास्क और अनुमोदन को केंद्र में जोड़ने वाला डेस्कटॉप व सेल्फ-होस्ट वर्कस्पेस।

- श्रेणी: वर्कस्पेस और कंटेक्स्ट असिस्टेंट; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: scheduled / webhook / manual routines।
- सीमा: प्रोजेक्ट शुरुआती चरण में है; सेल्फ-होस्ट सेवा और कंप्यूटर/ब्राउज़र क्षमताएँ प्रायोगिक हैं, होस्टेड संस्करण अलग उत्पाद है, मॉडल और अकाउंट उपयोगकर्ता को खुद जुटाने होंगे, और कुछ इंटीग्रेशन केवल Claude या Codex के साथ काम करते हैं।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 446 कमिट, 90 दिन में 817 कमिट।
- लाइसेंस: [Apache-2.0](https://api.github.com/repos/Anil-matcha/suparagent/license); GitHub licenseInfo ने पहचाना; होस्टेड सेवा, थर्ड-पार्टी इंजन, Composio और मॉडल प्रदाता अपनी-अपनी शर्तों पर चलते हैं।
- फ़ंक्शन सत्यापन: 2026-11-11; [स्रोत1](https://github.com/Anil-matcha/suparagent/blob/6fdd8ea6ccbe5d27edf5aff3a230a04ad3ee5ed9/README.md#L3) · [स्रोत2](https://github.com/Anil-matcha/suparagent/blob/6fdd8ea6ccbe5d27edf5aff3a230a04ad3ee5ed9/README.md#L71) · [स्रोत3](https://github.com/Anil-matcha/suparagent/blob/6fdd8ea6ccbe5d27edf5aff3a230a04ad3ee5ed9/README.md#L183)।

<a id="openbmb--pilotdeck"></a>

## [PilotDeck](https://github.com/OpenBMB/PilotDeck)

वर्कस्पेस के हिसाब से फ़ाइलें, स्मृति और स्किल अलग रखता है; बैकग्राउंड खोज-कार्य चलाकर फ़ाइल सौंपता है।

- श्रेणी: वर्कस्पेस और कंटेक्स्ट असिस्टेंट; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: always-on टास्क खोज।
- सीमा: README के benchmark लेखक-स्व-reported हैं; उन्हें इस निर्देशिका की क्रॉस-प्रोजेक्ट क्षमता-रैंकिंग में नहीं गिना जाता।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 468 कमिट, 90 दिन में 960 कमिट।
- लाइसेंस: [AGPL-3.0](https://api.github.com/repos/OpenBMB/PilotDeck/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/OpenBMB/PilotDeck/blob/2865f05b1722c7473ea8a9dda317a92fb8c92dd8/README.md#L97)।

<a id="copilotkit--openfuse"></a>

## [OpenFuse](https://github.com/CopilotKit/openfuse)

पर्सनल Agent इंटरफ़ेस, ब्राउज़र और वर्कस्पेस देने वाला ओपन-सोर्स ऐप।

- श्रेणी: वर्कस्पेस और कंटेक्स्ट असिस्टेंट; संलग्न क्षमताएँ।
- ट्रिगर: बैकग्राउंड टास्क worker; स्वतः ट्रिगर असत्यापित।
- सीमा: बैकग्राउंड worker का अर्थ स्वतः आरंभ नहीं; कुछ कनेक्टर और एक्शन अभी roadmap पर हैं।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 3 कमिट, 90 दिन में 147 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/CopilotKit/openfuse/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/CopilotKit/openfuse/blob/a4944f4c471d3dc93b8bfc060b5da309b5216ab2/README.md#L43)।

<a id="copilotkit--openduet"></a>

## [OpenDuet](https://github.com/CopilotKit/OpenDuet)

प्रैएक्टिव वर्क असिस्टेंट बनाने के लिए ओपन-सोर्स ऐप टेम्पलेट।

- श्रेणी: वर्कस्पेस और कंटेक्स्ट असिस्टेंट; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: routines / बैकग्राउंड सुझाव।
- सीमा: टेम्पलेट में निर्भरताएँ और मॉडल खुद कॉन्फ़िगर करने होंगे; यह पहले से तैनात होस्टेड सेवा नहीं है।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 24 कमिट, 90 दिन में 92 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/CopilotKit/OpenDuet/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/CopilotKit/OpenDuet/blob/f52288fff5ccdbd3de428d573d9f026fce5ff480/README.md#L5)।

<a id="volcengine--minecontext"></a>

## [MineContext](https://github.com/volcengine/MineContext)

स्क्रीन कंटेक्स्ट से अंतर्दृष्टि, to-do और दैनिक/साप्ताहिक सारांश बनाने वाला प्रैएक्टिव सूचना असिस्टेंट।

- श्रेणी: वर्कस्पेस और कंटेक्स्ट असिस्टेंट; संलग्न क्षमताएँ।
- ट्रिगर: कंटेक्स्ट अवलोकन / प्रैएक्टिव पुश।
- सीमा: प्रैएक्टिव सुझाव प्रमाणित हैं; इससे यह नहीं माना जाता कि यह सभी ऐप्स पर स्वतः संचालन कर सकता है।
- वर्तमान मेंटेनेंस स्थिति: 91–365 दिन बिना कमिट; 30 दिन में 0 कमिट, 90 दिन में 0 कमिट।
- लाइसेंस: [Apache-2.0](https://api.github.com/repos/volcengine/MineContext/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/volcengine/MineContext/blob/171c7a9ea8091e326ddcf0f10718aa1b58c83c65/README.md#L9)।

<a id="fei-craft--ds-bot"></a>

## [DS Bot](https://github.com/Fei-Craft/DS-Bot)

DeepSeek Harness को स्मृति, ग्रुप चैट और Bot सहयोग सहित डेस्कटॉप ऐप व प्लगइन में बदलता है।

- श्रेणी: प्रैएक्टिव प्लगइन और शेड्यूलिंग एक्सटेंशन; संलग्न क्षमताएँ।
- ट्रिगर: निरंतर Bot / ग्रुप चैट; स्वतः जागरण असत्यापित।
- सीमा: होमपेज पर स्वतंत्र शेड्यूल तंत्र की पुष्टि नहीं है; दीर्घकालिक सेशन को सीधे प्रैएक्टिव संचालन नहीं माना जा सकता।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 2844 कमिट, 90 दिन में 3858 कमिट।
- लाइसेंस: [Apache-2.0](https://api.github.com/repos/Fei-Craft/DS-Bot/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/Fei-Craft/DS-Bot/blob/71d344bf193f3f18185f25de3d8e5c483046910a/README.md#L41)।

<a id="john-walks-slow--dsh-proactive"></a>

## [dsh-proactive](https://github.com/john-walks-slow/dsh-proactive)

DeepSeek Harness में सेशन कोल्ड होने के बाद भी चलने वाला प्रैएक्टिव जागरण जोड़ता है।

- श्रेणी: प्रैएक्टिव प्लगइन और शेड्यूलिंग एक्सटेंशन; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: होस्ट-स्तरीय once / interval / cron।
- सीमा: होस्ट संचालन और संस्करण संगतता पर निर्भर; do-not-disturb और सूचना-बजट कॉन्फ़िगरेशन भी शामिल है।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 0 कमिट, 90 दिन में 97 कमिट।
- लाइसेंस: [MIT](https://github.com/john-walks-slow/dsh-proactive/blob/cae01f36b8aa6af2979ef138e9f8b2b62e6af0f9/packages/dsh-proactive/LICENSE); प्लगइन सबडायरेक्टरी के LICENSE का मानवीय सत्यापन।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/john-walks-slow/dsh-proactive/blob/cae01f36b8aa6af2979ef138e9f8b2b62e6af0f9/README.md#L1)।

<a id="t0dorakis--murmur"></a>

## [murmur](https://github.com/t0dorakis/murmur)

Claude, Codex, Pi आदि CLI सेशन को आवधिक जगाने वाला हल्का शेड्यूलर डीमन।

- श्रेणी: प्रैएक्टिव प्लगइन और शेड्यूलिंग एक्सटेंशन; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: cron / interval।
- सीमा: सूचना डिलीवरी और व्यावसायिक कार्य prompt तथा बुलाए गए Agent के हिस्से हैं।
- वर्तमान मेंटेनेंस स्थिति: 91–365 दिन बिना कमिट; 30 दिन में 0 कमिट, 90 दिन में 0 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/t0dorakis/murmur/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/t0dorakis/murmur/blob/d666df4c749c28ecb775613ecec8b12954b387e7/README.md#L10)।

<a id="hypostas--pulse"></a>

## [Pulse](https://github.com/Hypostas/pulse)

OpenClaw के लिए परिवर्तन, लक्ष्य और आपातता से जगाने वाला एक्सटेंशन डीमन।

- श्रेणी: प्रैएक्टिव प्लगइन और शेड्यूलिंग एक्सटेंशन; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: सेंसिंग / आपातता-ट्रिगर।
- सीमा: OpenClaw webhook पर निर्भर; लेखक का प्रैएक्टिवता वर्णन इस निर्देशिका का मापन-निष्कर्ष नहीं है।
- वर्तमान मेंटेनेंस स्थिति: 91–365 दिन बिना कमिट; 30 दिन में 0 कमिट, 90 दिन में 0 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/Hypostas/pulse/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/Hypostas/pulse/blob/4bebd1e23bff218dde1cd0b693f901493d45f972/README.md#L5)।

<a id="nousresearch--hermes-bot-mode"></a>

## [Hermes Bot Mode](https://github.com/NousResearch/Hermes-Bot-Mode)

Hermes डेस्कटॉप में नामेड Bot, अलग बातचीत और आवधिक टास्क पैनल जोड़ता है।

- श्रेणी: प्रैएक्टिव प्लगइन और शेड्यूलिंग एक्सटेंशन; ऐतिहासिक संदर्भ।
- ट्रिगर: होस्ट cron routines।
- सीमा: GitHub पर संग्रहित; केवल Hermes Bot UI और cron इंटीग्रेशन के संदर्भ के लिए रखा गया, सक्रिय प्लगइन अनुशंसा नहीं।
- वर्तमान मेंटेनेंस स्थिति: संग्रहित / ऐतिहासिक; 30 दिन में 0 कमिट, 90 दिन में 0 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/NousResearch/Hermes-Bot-Mode/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/NousResearch/Hermes-Bot-Mode/blob/80fee22582b871b9765a65e2992b8b5a8211c9f8/README.md#L23)।

<a id="earendil-works--pi"></a>

## [Pi](https://github.com/earendil-works/pi)

एक्सटेंसिबल Agent harness, जिसमें SDK, RPC और प्लगइन से सदैव-चालू असिस्टेंट बना सकते हैं।

- श्रेणी: एक्सटेंसिबल Harness और निरंतर संचालन आधार; संलग्न क्षमताएँ।
- ट्रिगर: ऊपरी शेड्यूलर / एक्सटेंशन चाहिए।
- सीमा: पुराना पता badlogic/pi-mono अब redirect होता है; rho या murmur के साथ जोड़ा जा सकता है।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 1378 कमिट, 90 दिन में 2364 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/earendil-works/pi/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/earendil-works/pi/blob/fcebc099565d8f30c15b321ff6a1af5f34d89400/README.md#L15)।

<a id="deepseek-ai--deepseek-harness"></a>

## [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)

प्लगइन आर्किटेक्चर से Agent संचालन आधार देता है; Bot और प्रैएक्टिव जागरण प्लगइन जोड़ने के लिए उपयुक्त।

- श्रेणी: एक्सटेंसिबल Harness और निरंतर संचालन आधार; संलग्न क्षमताएँ।
- ट्रिगर: प्रैएक्टिव तंत्र होस्ट प्लगइन से आना चाहिए।
- सीमा: developer preview; प्लगइन संगतता जाँचनी होगी।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 3743 कमिट, 90 दिन में 14426 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/deepseek-ai/deepseek-harness/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/deepseek-ai/deepseek-harness/blob/fcc0ad462172522aaf5c93a7b2e01f6b9f0b0159/README.md#L7)।

<a id="letta-ai--letta-code"></a>

## [Letta Code](https://github.com/letta-ai/letta-code)

स्थायी स्मृति वाला Agent, जिसमें remote environments और channels से सदैव-चालू असिस्टेंट बन सकता है।

- श्रेणी: एक्सटेंसिबल Harness और निरंतर संचालन आधार; प्रैएक्टिव तंत्र डॉक्यूमेंटेड।
- ट्रिगर: remote environments / cron।
- सीमा: LettaBot का आधिकारिक माइग्रेशन लक्ष्य; remote environment और शेड्यूल कॉन्फ़िगरेशन के साथ जोड़ना होगा।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 362 कमिट, 90 दिन में 978 कमिट।
- लाइसेंस: [Apache-2.0](https://api.github.com/repos/letta-ai/letta-code/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/letta-ai/letta-code/blob/e6d6cc27ef1111da80e919dc1cef179613894b66/README.md#L29) · [स्रोत2](https://docs.letta.com/letta-code/scheduling) · [स्रोत3](https://docs.letta.com/letta-code/scheduling)।

<a id="browser-use--browser-use"></a>

## [Browser Use](https://github.com/browser-use/browser-use)

Agent को वेब समझ और ब्राउज़र निष्पादन क्षमता देता है।

- श्रेणी: कंप्यूटर और ब्राउज़र कंट्रोल घटक; संलग्न क्षमताएँ।
- ट्रिगर: मांग पर ब्राउज़र कार्य।
- सीमा: मुख्यतः ब्राउज़र पर काम करता है; इससे प्रैएक्टिव शेड्यूलिंग या पूरे डेस्कटॉप नियंत्रण का सबूत नहीं मिलता।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 639 कमिट, 90 दिन में 954 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/browser-use/browser-use/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/browser-use/browser-use/blob/b49a68e4060acb226da8f784194fef301c53a6d7/README.md#L1)।

<a id="cursortouch--windows-mcp"></a>

## [Windows-MCP](https://github.com/CursorTouch/Windows-MCP)

Agent को Windows कंप्यूटर-संचालन क्षमताएँ देने वाली MCP सेवा।

- श्रेणी: कंप्यूटर और ब्राउज़र कंट्रोल घटक; संलग्न क्षमताएँ।
- ट्रिगर: होस्ट द्वारा कॉल।
- सीमा: स्वयं कंट्रोल घटक है, सदैव-चालू व्यक्तिगत असिस्टेंट नहीं; मॉडल, स्मृति और ट्रिगर बाहर से जोड़ने होंगे।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 110 कमिट, 90 दिन में 180 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/CursorTouch/Windows-MCP/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/CursorTouch/Windows-MCP/blob/9ab92bca2772dfb53ae3ed4feb98dac22c5b3dea/README.md#L25)।

<a id="alibaba--page-agent"></a>

## [Page Agent](https://github.com/alibaba/page-agent)

वेबपेज के अंदर प्राकृतिक भाषा से UI संभालने वाला JavaScript Agent।

- श्रेणी: कंप्यूटर और ब्राउज़र कंट्रोल घटक; संलग्न क्षमताएँ।
- ट्रिगर: वेबपेज या होस्ट द्वारा कॉल।
- सीमा: वेब-नियंत्रण परत; पूरी सदैव-चालू असिस्टेंट लाइफ़साइकिल नहीं रखती।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 22 कमिट, 90 दिन में 40 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/alibaba/page-agent/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/alibaba/page-agent/blob/9eb6b6646500264d9034dd466a4270cb9fc1ef1e/README.md#L35)।

<a id="bytedance--ui-tars-desktop"></a>

## [UI-TARS Desktop / Agent TARS](https://github.com/bytedance/UI-TARS-desktop)

GUI और ब्राउज़र संचालन देने वाले Agent ऐप और संबंधित उपकरण।

- श्रेणी: कंप्यूटर और ब्राउज़र कंट्रोल घटक; संलग्न क्षमताएँ।
- ट्रिगर: मांग पर कंप्यूटर / ब्राउज़र कार्य।
- सीमा: कंप्यूटर कार्य का ऑटो-एक्ज़ीक्यूशन और बिना निर्देश स्वतः आरंभ करना दो अलग आयाम हैं।
- वर्तमान मेंटेनेंस स्थिति: संग्रहित / ऐतिहासिक; 30 दिन में 0 कमिट, 90 दिन में 8 कमिट।
- लाइसेंस: [Apache-2.0](https://api.github.com/repos/bytedance/UI-TARS-desktop/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/README.md#L13)।

<a id="xlang-ai--osworld"></a>

## [OSWorld](https://github.com/xlang-ai/OSWorld)

असली कंप्यूटर वातावरण में मल्टीमोडल Agent के निष्पादन क्षमता का आकलन।

- श्रेणी: रिसर्च इम्प्लीमेंटेशन और इवैल्यूएशन कोड; शोध संसाधन।
- ट्रिगर: असली कंप्यूटर-टास्क इवैल्यूएशन।
- सीमा: कार्य-निष्पादन मापता है; स्वतः टास्क खोज और हस्तक्षेप-समय को अकेले नहीं माप सकता।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 70 कमिट, 90 दिन में 213 कमिट।
- लाइसेंस: [Apache-2.0](https://api.github.com/repos/xlang-ai/OSWorld/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/xlang-ai/OSWorld/blob/8903ebeb0efdf74331bd7dc37ed91ccbbff22317/README.md#L294)।

<a id="zju-real--knowu-bench"></a>

## [KnowU-Bench](https://github.com/ZJU-REAL/KnowU-Bench)

मोबाइल Agent द्वारा पसंद हासिल करना, प्रैएक्टिव हस्तक्षेप और अनुमति माँगना मापता है।

- श्रेणी: रिसर्च इम्प्लीमेंटेशन और इवैल्यूएशन कोड; शोध संसाधन।
- ट्रिगर: इंटरैक्टिव पर्सनलाइज़्ड मोबाइल इवैल्यूएशन।
- सीमा: मोबाइल GUI और व्यक्तिगत पसंद पर केंद्रित; सार्वभौमिक प्लेटफ़ॉर्म रनटाइम नहीं।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 1 कमिट, 90 दिन में 1 कमिट।
- लाइसेंस: [Apache-2.0](https://api.github.com/repos/ZJU-REAL/KnowU-Bench/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/ZJU-REAL/KnowU-Bench/blob/c03a825991ede13add6631f2ed19b90755930dc6/README.md#L4)।

<a id="facebookresearch--memo-pro-agent"></a>

## [MemoProAgent](https://github.com/facebookresearch/Memo-Pro-Agent)

दीर्घकालिक व्यक्तिगत स्मृति से प्रमाण खोजकर हस्तक्षेप-निर्णय शोधता है।

- श्रेणी: रिसर्च इम्प्लीमेंटेशन और इवैल्यूएशन कोड; शोध संसाधन।
- ट्रिगर: स्मृति-संचालित हस्तक्षेप इवैल्यूएशन।
- सीमा: पेपर का प्रारंभिक नाम ProPerAgent; एक ही arXiv ID से de-duplicate किया गया।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 0 कमिट, 90 दिन में 6 कमिट।
- लाइसेंस: [CC-BY-NC-4.0](https://github.com/facebookresearch/Memo-Pro-Agent/blob/8563e58d3106c8e0b3108bff64c04d00e1c8f095/LICENSE); ग़ैर-व्यावसायिक लाइसेंस; केवल शोध सोर्स-कोड के रूप में सूचीबद्ध।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/facebookresearch/Memo-Pro-Agent/blob/8563e58d3106c8e0b3108bff64c04d00e1c8f095/README.md#L3)।

<a id="simplified-reasoning--pi-bench"></a>

## [π-Bench](https://github.com/Simplified-Reasoning/Pi-Bench)

दीर्घकालिक मल्टी-टर्न वर्कफ़्लो में छिपी आवश्यकता पहचान और प्रैएक्टिव सहायता का आकलन।

- श्रेणी: रिसर्च इम्प्लीमेंटेशन और इवैल्यूएशन कोड; शोध संसाधन।
- ट्रिगर: प्रैएक्टिवनेस इवैल्यूएशन।
- सीमा: यह benchmark है; Pi harness से इसका कोई संबंध नहीं।
- वर्तमान मेंटेनेंस स्थिति: पिछले 90 दिनों में कमिट; 30 दिन में 0 कमिट, 90 दिन में 1 कमिट।
- लाइसेंस: [Apache-2.0](https://api.github.com/repos/Simplified-Reasoning/Pi-Bench/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/Simplified-Reasoning/Pi-Bench/blob/4f545be5d289b28ff022d2904d455007358ed3b7/README.md#L1)।

<a id="thunlp--proactiveagent"></a>

## [ProactiveAgent](https://github.com/thunlp/ProactiveAgent)

प्रैएक्टिव टास्क-पूर्वानुमान विधि तथा उसका डेटा और इवैल्यूएशन कोड।

- श्रेणी: रिसर्च इम्प्लीमेंटेशन और इवैल्यूएशन कोड; शोध संसाधन।
- ट्रिगर: इवेंट अवलोकन / टास्क पूर्वानुमान।
- सीमा: रिसर्च इम्प्लीमेंटेशन; तैयार सार्वभौमिक व्यक्तिगत असिस्टेंट के बराबर नहीं।
- वर्तमान मेंटेनेंस स्थिति: 91–365 दिन बिना कमिट; 30 दिन में 0 कमिट, 90 दिन में 0 कमिट।
- लाइसेंस: [Apache-2.0](https://api.github.com/repos/thunlp/ProactiveAgent/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/thunlp/ProactiveAgent/blob/3fcf9beebe256b86871659fbb12541c41c9381b9/README.md#L2)।

<a id="xzf-thu--pask"></a>

## [PASK](https://github.com/xzf-thu/Pask)

दीर्घकालिक स्मृति, निरंतर कंटेक्स्ट और latency बाधाओं को मिलाकर प्रैएक्टिव सहायता शोधता है।

- श्रेणी: रिसर्च इम्प्लीमेंटेशन और इवैल्यूएशन कोड; शोध संसाधन।
- ट्रिगर: संभावित आवश्यकता पहचान / चुप रहना।
- सीमा: तकनीकी रिपोर्ट और रिसर्च कोड; व्यावहारिक परिपक्वता अलग से जाँचनी होगी।
- वर्तमान मेंटेनेंस स्थिति: 91–365 दिन बिना कमिट; 30 दिन में 0 कमिट, 90 दिन में 0 कमिट।
- लाइसेंस: [Apache-2.0](https://api.github.com/repos/xzf-thu/Pask/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/xzf-thu/Pask/blob/d54646c52b1555232ce4ab39103768d7f65b8267/README.md#L30)।

<a id="deepakn97--pare"></a>

## [PARE](https://github.com/deepakn97/pare)

प्रैएक्टिव उपयोगकर्ता और stateful डिजिटल वातावरण के सिमुलेशन से प्रैएक्टिव असिस्टेंट का आकलन।

- श्रेणी: रिसर्च इम्प्लीमेंटेशन और इवैल्यूएशन कोड; शोध संसाधन।
- ट्रिगर: प्रैएक्टिव असिस्टेंट / उपयोगकर्ता सिमुलेशन इवैल्यूएशन।
- सीमा: सिमुलेटेड उपयोगकर्ता वास्तविक उपयोगकर्ता के दीर्घकालिक प्रभाव के बराबर नहीं।
- वर्तमान मेंटेनेंस स्थिति: 91–365 दिन बिना कमिट; 30 दिन में 0 कमिट, 90 दिन में 0 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/deepakn97/pare/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/deepakn97/pare/blob/261149914a9e9dcacb12de620575c691d50e3c2e/README.md#L3)।

<a id="tdemin16--proactivebench"></a>

## [ProactiveBench (MLLM)](https://github.com/tdemin16/proactivebench)

मल्टीमोडल मॉडलों द्वारा उपयोगी सूचना का प्रैएक्टिव संग्रह मापने वाला रिसर्च benchmark।

- श्रेणी: रिसर्च इम्प्लीमेंटेशन और इवैल्यूएशन कोड; शोध संसाधन।
- ट्रिगर: मल्टीमोडल प्रैएक्टिवनेस इवैल्यूएशन।
- सीमा: ProactiveAgent के समान-नाम वाले benchmark से अलग; आधिकारिक पेपर पेज पर ECCV 2026 दर्ज है।
- वर्तमान मेंटेनेंस स्थिति: 91–365 दिन बिना कमिट; 30 दिन में 0 कमिट, 90 दिन में 0 कमिट।
- लाइसेंस: [MIT](https://api.github.com/repos/tdemin16/proactivebench/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/tdemin16/proactivebench/blob/428885c9224418b544dfbdbde5307bccc58018d5/README.md#L2)।

<a id="openaiotlab--contextagent"></a>

## [ContextAgent](https://github.com/openaiotlab/ContextAgent)

खुले-वातावरण की सेंसिंग सूचना से प्रैएक्टिव सेवा और टूल-कॉल का निर्णय शोधता है।

- श्रेणी: रिसर्च इम्प्लीमेंटेशन और इवैल्यूएशन कोड; शोध संसाधन।
- ट्रिगर: सेंसिंग कंटेक्स्ट / सेवा पूर्वानुमान।
- सीमा: रिसर्च डेटा और टूल परिदृश्यों को सीधे किसी भी डेस्कटॉप पर सामान्यीकृत नहीं किया जा सकता।
- वर्तमान मेंटेनेंस स्थिति: 91–365 दिन बिना कमिट; 30 दिन में 0 कमिट, 90 दिन में 0 कमिट।
- लाइसेंस: [असत्यापित](https://github.com/openaiotlab/ContextAgent/blob/f4674bf2a1385ce829c6a7f2ea9c53871dd1a8ce/README.md); LICENSE नहीं मिला; केवल शोध संसाधन, अनुमति का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/openaiotlab/ContextAgent/blob/f4674bf2a1385ce829c6a7f2ea9c53871dd1a8ce/README.md#L3)।

<a id="letta-ai--lettabot"></a>

## [LettaBot](https://github.com/letta-ai/lettabot)

मैसेज चैनल, स्मृति, heartbeat और शेड्यूल टास्क देने वाला व्यक्तिगत असिस्टेंट।

- श्रेणी: ऐतिहासिक और माइग्रेशन प्रोजेक्ट; ऐतिहासिक संदर्भ।
- ट्रिगर: heartbeat / cron।
- सीमा: आधिकारिक README ने सक्रिय मेंटेनेंस बंद करने की घोषणा कर दी है और Letta Code पर माइग्रेशन सुझाया है।
- वर्तमान मेंटेनेंस स्थिति: संग्रहित / ऐतिहासिक; 30 दिन में 0 कमिट, 90 दिन में 0 कमिट।
- लाइसेंस: [Apache-2.0](https://api.github.com/repos/letta-ai/lettabot/license); GitHub licenseInfo ने पहचाना; सहलग्न डेटा या मॉडल वेट के लाइसेंस का अनुमान नहीं लगाया जाता।
- फ़ंक्शन सत्यापन: 2026-11-05; [स्रोत1](https://github.com/letta-ai/lettabot/blob/99c3b5dd73550fe0a4eac2ee31b1c3229ca9e550/README.md#L8)।
