import React from "react"
import { GiHamburgerMenu } from "react-icons/gi"

function Header({ title }) {
  return (
    <header className="header">
      {title}

      <GiHamburgerMenu className="burger-menu" onClick={() => {}} />
    </header>
  )
}

export default Header
