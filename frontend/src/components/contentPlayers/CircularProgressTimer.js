"use client";

import { formatDuration } from "@/utils";
import { useState, useEffect } from "react";

const FULL_DASH_ARRAY = 283;
const TIME_LIMIT = 60; // seconds

export default function CircularProgressTimer({
  callback,
  duration = TIME_LIMIT,
}) {
  const [timeLeft, setTimeLeft] = useState(duration);
  const [offset, setOffset] = useState(FULL_DASH_ARRAY);

  useEffect(() => {
    if (timeLeft === 0) {
      if (callback) {
        callback();
      }
      return;
    }

    const timerInterval = setInterval(() => {
      setTimeLeft((prevTime) => {
        const newTime = prevTime - 1;
        setOffset((newTime / duration) * FULL_DASH_ARRAY);
        if (newTime === 0) {
          clearInterval(timerInterval);
        }
        return newTime;
      });
    }, 1000);

    return () => clearInterval(timerInterval);
  }, [timeLeft]);

  return (
    <div className="relative w-24 h-24">
      <svg
        className="absolute inset-0 transform rotate-[-90deg]"
        width="100"
        height="100"
      >
        <circle
          cx="50"
          cy="50"
          r="45"
          className="stroke-gray-100 fill-none stroke-[5]"
        />
        <circle
          cx="50"
          cy="50"
          r="45"
          className="progress stroke-sky-400 fill-none stroke-[5]"
          style={{
            strokeDasharray: FULL_DASH_ARRAY,
            strokeDashoffset: FULL_DASH_ARRAY - offset,
          }}
        />
      </svg>
      <div className="absolute inset-0 flex items-center justify-center text-md font-bold text-gray-300">
        {formatDuration(`${timeLeft}s`)}
      </div>
    </div>
  );
}
