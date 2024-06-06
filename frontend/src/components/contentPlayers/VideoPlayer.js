"use client";

import { getMediaAbsolutePath } from "@/utils";
import CircularProgressTimer from "./CircularProgressTimer";
import ReactPlayer from "react-player";

export default function VideoPlayer({ content, switchContent }) {
  return (
    <main className="flex min-h-screen flex-col items-center">
      <video width="100%" height="100%" autoPlay={true} muted>
        <source src={getMediaAbsolutePath(content.file)} />
        Your browser does not support the video tag.
      </video>
      <div className="absolute bottom-4 right-4">
        <CircularProgressTimer
          duration={content.duration}
          callback={switchContent}
        />
      </div>
    </main>
  );
}
