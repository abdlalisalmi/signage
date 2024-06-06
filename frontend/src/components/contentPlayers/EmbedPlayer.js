"use client";

import { useState } from "react";
import { getMediaAbsolutePath } from "@/utils";
import CircularProgressTimer from "./CircularProgressTimer";
import ReactPlayer from "react-player";

export default function EmbedPlayer({ content, switchContent }) {
  const [duration, setDuration] = useState(0);
  const [playing, setPlaying] = useState(true);

  console.log("duration: ", duration);
  console.log("playing: ", playing);
  const handleDuration = (duration) => {
    setDuration(duration);
  };
  return (
    <main className="flex min-h-screen flex-col items-center">
      <ReactPlayer
        width={"100%"}
        height={"100vh"}
        url={content.url}
        playing={playing}
        onPlay={() => setPlaying(true)}
        onReady={() => setPlaying(true)}
        onSeek={(e) => console.log("onSeek", e)}
        onDuration={handleDuration}
        onEnded={switchContent}
        onError={switchContent}
      />
      <div className="absolute bottom-4 right-4">
        {duration > 0 && (
          <CircularProgressTimer
            key={duration}
            duration={duration + 3}
            callback={switchContent}
          />
        )}
      </div>
    </main>
  );
}
