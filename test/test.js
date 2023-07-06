const { Builder, By, Key, until } = require("selenium-webdriver");
require("chromedriver");
const fs = require("fs");
const file_contents = fs.readFileSync(
  `C://Users//jasbi//Desktop//creds.txt`,
  "utf-8"
);
const lines = file_contents.split("\n");
const username = lines[0];
const password = lines[1];

async function example() {
  let driver = await new Builder().forBrowser("chrome").build();
  try {
    await driver.get("https://www.linkedin.com/uas/login");
    await driver.findElement(By.id("username")).sendKeys(username);
    await driver.findElement(By.id("password")).sendKeys(password);
    await driver
      .findElement(By.xpath(`//*[@id="organic-div"]/form/div[3]`))
      .click();
    await driver.get("https://www.linkedin.com/mynetwork/");

    try {
      const button = driver.wait(
        until.elementLocated(
          By.xpath(
            `/html/body/div[6]/div[3]/div/div/div/div/div[2]/div/div/main/ul/li[2]/div/button`
          )
        )
      );
      await driver.wait(until.elementIsEnabled(button), 10000);
      await driver.executeScript("arguments[0].click();", button);
      await new Promise((r) => setTimeout(r, 5000));
    } catch (e) {
      // await driver.findElement(By.id(`ember312`)).click();
      console.log(e);
    }
    // find all spans which say "connect" and get their button parents

    try {
      // for (let i = 0; i < 10; ++i) {
      await driver.executeScript(
        "document.querySelector('.scaffold-finite-scroll__content').scrollDown += 100"
      );
      // }n

      // const buttons = await driver.findElements(By.css("button"));
      // for (let button of buttons) {
      //   const childSpans = await button.findElements(By.css("span"));
      //   for (let span of childSpans) {
      //     const spanText = await span.getText();
      //     if (spanText === "Connect") {
      //       // await button.click();
      //       // await new Promise((r) => setTimeout(r, 1000));

      //       break;
      //     }
      //   }
      // }
    } catch (e) {}

    driver.findElements();
    await new Promise((r) => setTimeout(r, 20000000));
  } catch (e) {
    console.log(e);
  } finally {
    await driver.quit();
  }
}

example();
