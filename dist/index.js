import "./styles/main.css.proxy.js";
import {startApp} from "../web_modules/narrat.js";
window.addEventListener("load", () => {
  startApp({
    charactersPath: "data/characters.json",
    configPath: "data/config.json"
  }, {
    debug: true,
    logging: false
  });
});
