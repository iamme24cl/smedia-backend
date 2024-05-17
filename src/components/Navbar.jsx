import React from 'react';
import { AppBar, styled, Typography, Toolbar } from '@mui/material';
import NewspaperIcon from '@mui/icons-material/Newspaper';

const StyledToolbar = styled(Toolbar)({
    display: "flex",
    justifyContent: "space-between"
})

const Navbar = () => {
  return (
    <AppBar position='stick'>
        <StyledToolbar>
            <Typography variant='h6' sx={{ display: {xs:"none", sm:"block"}}}>sMedia</Typography>
            <NewspaperIcon sx={{ display: {xs:"block", sm:"none"}}} />
        </StyledToolbar>
    </AppBar>
  );
}

export default Navbar;