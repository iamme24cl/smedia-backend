import React, { useState } from 'react';
import { 
    Avatar,
    Button,
    ButtonGroup,
    Fab,
    Modal,
    Stack,
    styled,
    TextField,
    Tooltip,
    Typography,
    Box,
} from '@mui/material';
import { 
    Add as AddIcon,
    DateRange,
    EmojiEmotions,
    Image,
    PersonAdd,
    VideoCameraBack,
 } from '@mui/icons-material';

const StyledModal = styled(Modal)({
    display: "flex",
    alignItems: "center",
    justifyContent: 'center',
});

const UserBox = styled(Box)({
    display: "flex",
    gap: "10px",
    alignItems: "center",
    marginBottom: "20px",
});

const Add = () => {
    const [open, setOpen] = useState(false);

  return (
    <>
        <Tooltip 
            onClick={(e) => setOpen(true)}
            title="add" 
            sx={{ 
                position: "fixed", 
                bottom: 30, 
                left: { xs: "calc(50% - 25px)", md: 30 },
            }}
        >
            <Fab color="primary" aria-label="add">
                <AddIcon />
            </Fab>
        </Tooltip>
        <StyledModal
            open={open}
            onClose={(e) => setOpen(false)}
            aria-labelledby="modal-modal-title"
            aria-describedby="modal-modal-description"
        >
            <Box
                width={400}
                height={280}
                bgcolor={"background.default"}
                color={"text.primary"}
                p={3}
                borderRadius={5}
            >
                <Typography variant='h6' color={"gray"} textAlign={"center"}>
                    Create Post
                </Typography>
                <UserBox>
                    <Avatar 
                        src='https://randomuser.me/api/portraits/thumb/men/17.jpg'
                        sx={{ width: 30, height: 30 }}
                    />
                    <Typography fontWeight={500} variant='span'>
                        John Doe
                    </Typography>
                </UserBox>
                <TextField 
                    sx={{ width: "100%" }}
                    id='standard-multiline-static'
                    multiline
                    rows={3}
                    placeholder="What's on your mind?"
                    variant='standard'
                />
                <Stack direction={"row"} gap={1} mt={2} mb={3}>
                    <EmojiEmotions sx={{ cursor: "pointer" }} color="primary" />
                    <Image sx={{ cursor: "pointer" }} color="secondary" />
                    <VideoCameraBack sx={{ cursor: "pointer" }} color="success" />
                    <PersonAdd sx={{ cursor: "pointer" }} color="error" />
                </Stack>
                <ButtonGroup
                    fullWidth
                    variant='contained'
                    aria-label='outlined primary button group'
                >
                    <Button>Post</Button>
                    <Button sx={{ width: "100px" }}>
                        <DateRange />
                    </Button>
                </ButtonGroup>
            </Box>
        </StyledModal>
    </>
  );
}

export default Add;