import React from "react";
import Header from "./components/header";
import Main from "./components/main";

class App extends React.Component {
	constructor(props) {
		super(props)
		this.state = {}
	}

		render () {
		return (<div>
				<Header title="Document formatting"/>
				<Main />
			</div>
		)
	}



}

export default App