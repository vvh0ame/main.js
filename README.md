# main.js
Mobile-API for [MAIN](https://play.google.com/store/apps/details?id=is.mdk.app) crypto social network

## Example
```JavaScript
async function main() {
	const { Main } = require("./main.js")
	const main = new Main()
	await main.loginWithGoogle("googleIdToken")
}

main()
```
