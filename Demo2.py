{
  "id": "a42f1c4d-c8f6-40bb-b711-b02d0cffe7a9",
  "version": "2.0",
  "name": "Demo 2",
  "url": "https://opensource-demo.orangehrmlive.com",
  "tests": [{
    "id": "32c26ff1-3f5f-4acd-92a1-6fe7b53ef7c4",
    "name": "TC1",
    "commands": [{
      "id": "2d920863-b573-4996-babd-283446589aae",
      "comment": "",
      "command": "open",
      "target": "/web/index.php/dashboard/index",
      "targets": [],
      "value": ""
    }, {
      "id": "2a18a56d-ee9e-45ee-9702-d18104c99407",
      "comment": "",
      "command": "setWindowSize",
      "target": "1936x1048",
      "targets": [],
      "value": ""
    }, {
      "id": "db843c33-d0a6-4f8d-bc25-42ebf563cb08",
      "comment": "",
      "command": "click",
      "target": "linkText=Admin",
      "targets": [
        ["linkText=Admin", "linkText"],
        ["css=.oxd-main-menu-item-wrapper:nth-child(1) > .oxd-main-menu-item", "css:finder"],
        ["xpath=//div[@id='app']/div/div/aside/nav/div[2]/ul/li/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, '/web/index.php/admin/viewAdminModule')]", "xpath:href"],
        ["xpath=//li/a", "xpath:position"],
        ["xpath=//a[contains(.,'Admin')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "c6d81614-7e1f-433d-b2bd-cef3816d162d",
      "comment": "",
      "command": "mouseOver",
      "target": "linkText=Admin",
      "targets": [
        ["linkText=Admin", "linkText"],
        ["css=.active", "css:finder"],
        ["xpath=//div[@id='app']/div/div/aside/nav/div[2]/ul/li/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, '/web/index.php/admin/viewAdminModule')]", "xpath:href"],
        ["xpath=//li/a", "xpath:position"],
        ["xpath=//a[contains(.,'Admin')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "14c60110-9b93-4c5e-bde2-ee525e453f53",
      "comment": "",
      "command": "mouseOut",
      "target": "linkText=Admin",
      "targets": [
        ["linkText=Admin", "linkText"],
        ["css=.active", "css:finder"],
        ["xpath=//div[@id='app']/div/div/aside/nav/div[2]/ul/li/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, '/web/index.php/admin/viewAdminModule')]", "xpath:href"],
        ["xpath=//li/a", "xpath:position"],
        ["xpath=//a[contains(.,'Admin')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "9cdd5221-68ca-4710-b6b6-620cd2f87528",
      "comment": "",
      "command": "click",
      "target": "css=.oxd-input--focus",
      "targets": [
        ["css=.oxd-input--focus", "css:finder"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/input", "xpath:idRelative"],
        ["xpath=//div[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "2dac004d-95d6-4d44-b0dc-54ba2d873cfe",
      "comment": "",
      "command": "click",
      "target": "css=.oxd-input--focus",
      "targets": [
        ["css=.oxd-input--focus", "css:finder"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/input", "xpath:idRelative"],
        ["xpath=//div[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "e69d2a4a-900e-4381-995e-6a079c28b75b",
      "comment": "",
      "command": "type",
      "target": "css=.oxd-input--focus",
      "targets": [
        ["css=.oxd-input--focus", "css:finder"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/input", "xpath:idRelative"],
        ["xpath=//div[2]/input", "xpath:position"]
      ],
      "value": "FMLName"
    }, {
      "id": "e09583d6-adc9-4931-8e43-f78f87d0a174",
      "comment": "",
      "command": "click",
      "target": "css=.oxd-select-text--focus > .oxd-select-text-input",
      "targets": [
        ["css=.oxd-select-text--focus > .oxd-select-text-input", "css:finder"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[2]/div/div[2]/div/div/div", "xpath:idRelative"],
        ["xpath=//div[2]/div/div[2]/div/div/div", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "52ac1a06-7d85-430e-9523-f64d67b3a1bb",
      "comment": "",
      "command": "click",
      "target": "css=.oxd-autocomplete-text-input > input",
      "targets": [
        ["css=.oxd-autocomplete-text-input > input", "css:finder"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[3]/div/div[2]/div/div/input", "xpath:idRelative"],
        ["xpath=//div/div[2]/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "73f1bc91-416b-4a57-b2cf-ff6d198c2fbd",
      "comment": "",
      "command": "type",
      "target": "css=.oxd-autocomplete-text-input > input",
      "targets": [
        ["css=.oxd-autocomplete-text-input > input", "css:finder"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[3]/div/div[2]/div/div/input", "xpath:idRelative"],
        ["xpath=//div/div[2]/div/div/input", "xpath:position"]
      ],
      "value": "Qwerty Qwerty LName"
    }, {
      "id": "a9fa5c73-b08d-4f0a-a0a6-205de3052fc8",
      "comment": "",
      "command": "click",
      "target": "css=.oxd-select-text--focus > .oxd-select-text-input",
      "targets": [
        ["css=.oxd-select-text--focus > .oxd-select-text-input", "css:finder"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[4]/div/div[2]/div/div/div", "xpath:idRelative"],
        ["xpath=//div[4]/div/div[2]/div/div/div", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "1933cfe7-0476-4c9d-8415-6ea1a13cae0b",
      "comment": "",
      "command": "click",
      "target": "css=.orangehrm-left-space",
      "targets": [
        ["css=.orangehrm-left-space", "css:finder"],
        ["xpath=//button[@type='submit']", "xpath:attributes"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button[2]", "xpath:idRelative"],
        ["xpath=//button[2]", "xpath:position"],
        ["xpath=//button[contains(.,'Search')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "bef8eb3d-970f-4915-b14c-00acdfe60285",
      "comment": "",
      "command": "click",
      "target": "css=.oxd-button--ghost",
      "targets": [
        ["css=.oxd-button--ghost", "css:finder"],
        ["xpath=(//button[@type='button'])[5]", "xpath:attributes"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button", "xpath:idRelative"],
        ["xpath=//div[2]/button", "xpath:position"],
        ["xpath=//button[contains(.,'Reset')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "10b571a5-f412-422a-bbc5-2af8a1c8b468",
      "comment": "",
      "command": "mouseDownAt",
      "target": "css=html",
      "targets": [
        ["css=html", "css:finder"],
        ["xpath=//html", "xpath:position"]
      ],
      "value": "1912,501"
    }, {
      "id": "f21814ed-7139-42e6-a8ff-69effe134a67",
      "comment": "",
      "command": "mouseMoveAt",
      "target": "css=html",
      "targets": [
        ["css=html", "css:finder"],
        ["xpath=//html", "xpath:position"]
      ],
      "value": "1912,501"
    }, {
      "id": "f45b11ab-0691-4f59-a696-8346bc032857",
      "comment": "",
      "command": "mouseUpAt",
      "target": "css=html",
      "targets": [
        ["css=html", "css:finder"],
        ["xpath=//html", "xpath:position"]
      ],
      "value": "1912,501"
    }, {
      "id": "764af43f-b08c-4681-93f3-e077c4b6df46",
      "comment": "",
      "command": "mouseDownAt",
      "target": "css=html",
      "targets": [
        ["css=html", "css:finder"],
        ["xpath=//html", "xpath:position"]
      ],
      "value": "1911,398"
    }, {
      "id": "2ea07c06-deb3-4cb6-b3e3-492c3c405b1d",
      "comment": "",
      "command": "mouseMoveAt",
      "target": "css=html",
      "targets": [
        ["css=html", "css:finder"],
        ["xpath=//html", "xpath:position"]
      ],
      "value": "1911,398"
    }, {
      "id": "c604d86e-a551-4589-8fb8-a84f052d8494",
      "comment": "",
      "command": "mouseUpAt",
      "target": "css=html",
      "targets": [
        ["css=html", "css:finder"],
        ["xpath=//html", "xpath:position"]
      ],
      "value": "1911,398"
    }, {
      "id": "b6873362-6ec4-4435-b446-df278554db63",
      "comment": "",
      "command": "click",
      "target": "css=.oxd-input--focus",
      "targets": [
        ["css=.oxd-input--focus", "css:finder"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/input", "xpath:idRelative"],
        ["xpath=//div[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "e10705dc-3b22-462d-9e19-b1ba62187711",
      "comment": "",
      "command": "type",
      "target": "css=.oxd-input--focus",
      "targets": [
        ["css=.oxd-input--focus", "css:finder"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/input", "xpath:idRelative"],
        ["xpath=//div[2]/input", "xpath:position"]
      ],
      "value": "user_013"
    }, {
      "id": "970b3f79-4259-4cc3-aff5-6255e0de40bb",
      "comment": "",
      "command": "click",
      "target": "css=.orangehrm-left-space",
      "targets": [
        ["css=.orangehrm-left-space", "css:finder"],
        ["xpath=//button[@type='submit']", "xpath:attributes"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button[2]", "xpath:idRelative"],
        ["xpath=//button[2]", "xpath:position"],
        ["xpath=//button[contains(.,'Search')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "f8e577d9-adc6-451e-87e9-6df1da8aff43",
      "comment": "",
      "command": "click",
      "target": "css=.oxd-input--focus",
      "targets": [
        ["css=.oxd-input--focus", "css:finder"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/input", "xpath:idRelative"],
        ["xpath=//div[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "0084b57c-81b5-4e9d-921c-426afd788961",
      "comment": "",
      "command": "click",
      "target": "css=.oxd-input--focus",
      "targets": [
        ["css=.oxd-input--focus", "css:finder"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/input", "xpath:idRelative"],
        ["xpath=//div[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "f8c6d90b-9993-471b-bea6-7ee2541151b7",
      "comment": "",
      "command": "doubleClick",
      "target": "css=.oxd-input--focus",
      "targets": [
        ["css=.oxd-input--focus", "css:finder"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/input", "xpath:idRelative"],
        ["xpath=//div[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "c85dbc09-8e00-48b5-9f88-ffff64a548af",
      "comment": "",
      "command": "click",
      "target": "css=.oxd-input--focus",
      "targets": [
        ["css=.oxd-input--focus", "css:finder"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/input", "xpath:idRelative"],
        ["xpath=//div[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "d95fcdc5-81ee-482d-be25-ad1a66f5e9d3",
      "comment": "",
      "command": "click",
      "target": "css=.oxd-button--ghost",
      "targets": [
        ["css=.oxd-button--ghost", "css:finder"],
        ["xpath=(//button[@type='button'])[5]", "xpath:attributes"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button", "xpath:idRelative"],
        ["xpath=//div[2]/button", "xpath:position"],
        ["xpath=//button[contains(.,'Reset')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "981fa479-1e89-453f-99b0-00ac045cd89f",
      "comment": "",
      "command": "click",
      "target": "css=.oxd-autocomplete-text-input > input",
      "targets": [
        ["css=.oxd-autocomplete-text-input > input", "css:finder"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[3]/div/div[2]/div/div/input", "xpath:idRelative"],
        ["xpath=//div/div[2]/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "26d14415-720c-4a63-9019-06e78454caf1",
      "comment": "",
      "command": "type",
      "target": "css=.oxd-autocomplete-text-input > input",
      "targets": [
        ["css=.oxd-autocomplete-text-input > input", "css:finder"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[3]/div/div[2]/div/div/input", "xpath:idRelative"],
        ["xpath=//div/div[2]/div/div/input", "xpath:position"]
      ],
      "value": "Carol E. Davis"
    }, {
      "id": "ff2c69e3-9b95-4309-87be-59f12547011b",
      "comment": "",
      "command": "click",
      "target": "css=.orangehrm-left-space",
      "targets": [
        ["css=.orangehrm-left-space", "css:finder"],
        ["xpath=//button[@type='submit']", "xpath:attributes"],
        ["xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button[2]", "xpath:idRelative"],
        ["xpath=//button[2]", "xpath:position"],
        ["xpath=//button[contains(.,'Search')]", "xpath:innerText"]
      ],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "91b570fa-b1b1-4016-b7d7-57978634a572",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["32c26ff1-3f5f-4acd-92a1-6fe7b53ef7c4"]
  }],
  "urls": ["https://opensource-demo.orangehrmlive.com/"],
  "plugins": []
}