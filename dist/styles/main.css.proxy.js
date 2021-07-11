// [snowpack] add styles to the page (skip if no document exists)
if (typeof document !== 'undefined') {
  const code = ".dialog-picture.override {\r\n  width: 200px;\r\n  height: 332px;\r\n  bottom: 180px;\r\n  left: -185px;\r\n}\r\n\r\n";

  const styleEl = document.createElement("style");
  const codeEl = document.createTextNode(code);
  styleEl.type = 'text/css';
  styleEl.appendChild(codeEl);
  document.head.appendChild(styleEl);
}