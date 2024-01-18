import React from "react";
import { GiHamburgerMenu } from "react-icons/gi";



class Header extends React.Component {
	render () {
		return(
			<header className="header">
				
				{this.props.title}

				<GiHamburgerMenu className="burger-menu" onClick={() => {}} />
			</header>
		)
	}
}

export default Header