import { Stack , VStack ,Heading, Text , Button} from '@chakra-ui/react'
import React, { useState } from 'react'
 

const Video = () => {
    const videosArr= ['https://streamable.com/f31tbi',
    'https://streamable.com/f31tbi',
    'https://streamable.com/f31tbi',
    'https://streamable.com/f31tbi',
    'https://streamable.com/f31tbi',
    'https://streamable.com/f31tbi']
  const [videoSrc,  setVideoSrc]= useState(videosArr[0])
  return (
    <Stack direction={['column', 'row']} h={'100vh'}>
        <VStack w={'full'}>
           <video controls controlsList='nodownload' src={videoSrc} style={{
                width:"100%"
           }}></video>

           <VStack alignItems={'flex-start'} p={'8'} w={'full'} overflowY={'auto'}>
            <Heading>Sample Video 1</Heading>
            <Text>This is a sample video for testing and demo.</Text>
           </VStack>
        </VStack>
        <VStack w={['full','xl']} alignItems={'stretch'} p={'8'} spacing={'8'} overflowY={'auto'}>
          {
            videosArr.map((item,index)=>(
                <Button variant={'ghost'} colorScheme={'purple'} onClick={()=>setVideoSrc(item)}>Lecture {index+1}</Button>
            ))
          }
        </VStack>
    </Stack>
  )
}

export default Video
