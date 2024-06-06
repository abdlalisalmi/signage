"use client";

import { useState, useEffect, useRef } from "react";
import { PiScreencastFill } from "react-icons/pi";
import CircularProgressTimer from "./CircularProgressTimer";

export default function EmptyContents() {
  const callback = () => {
    window.location.reload();
  };
  return (
    <main className="flex min-h-screen flex-col items-center justify-center w-full">
      <section className="w-full h-full">
        <div className="flex flex-col items-center justify-center h-full">
          <div className="text-4xl text-gray-400">
            <PiScreencastFill />
          </div>
          <div className="text-sm text-gray-400">No content available</div>
        </div>
        <div className="absolute bottom-4 right-4">
          <CircularProgressTimer callback={callback} />
        </div>
      </section>
    </main>
  );
}
