"use client";

import { getMediaAbsolutePath } from "@/utils";
import CircularProgressTimer from "./CircularProgressTimer";

export default function ImagePlayer({ content, switchContent }) {
  return (
    <main className="flex min-h-screen flex-col items-center">
      <img
        src={getMediaAbsolutePath(content.file)}
        alt={content.name}
        className="w-screen h-screen"
      />
      <div className="absolute bottom-4 right-4">
        <CircularProgressTimer
          duration={content.duration}
          callback={switchContent}
        />
      </div>
    </main>
  );
}
