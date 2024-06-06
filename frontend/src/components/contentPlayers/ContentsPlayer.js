"use client";

import { useState, useEffect } from "react";
import CustomLoader from "@/components/CustomLoader";
import ImagePlayer from "./ImagePlayer";
import VideoPlayer from "./videoPlayer";
import EmbedPlayer from "./embedPlayer";
import TextPlayer from "./TextPlayer";

export default function ContentsPlayer({ initialContents }) {
  const [contents, setContents] = useState(initialContents);
  const [activeContent, setActiveContent] = useState(null);
  const [loading, setLoading] = useState(true);
  const [uniqueKey, setUniqueKey] = useState(0); // Unique key state to force re-render
  const [contentsCount, setContentsCount] = useState(initialContents.length); // Total contents count state
  const [currentIndex, setCurrentIndex] = useState(0); // Index tracker state

  const switchContent = () => {
    setLoading(true);
    if (contents.length === 0) {
      window.location.reload();
      //   alert("End of contents");
    } else {
      const newContents = [...contents];
      const nextContent = newContents.pop();

      setActiveContent(nextContent);
      setContents(newContents);
      setUniqueKey((prevKey) => prevKey + 1); // Update the unique key
      setCurrentIndex((prevIndex) => prevIndex + 1);
    }

    setLoading(false);
  };

  useEffect(() => {
    switchContent();
  }, []);

  if (loading) {
    return (
      <main className="flex min-h-screen flex-col items-center justify-center">
        <CustomLoader />
      </main>
    );
  }

  return (
    <main key={uniqueKey}>
      <div className="absolute bottom-4 left-4">
        <p className="text-gray-300 text-xl font-bold">
          {currentIndex}/{contentsCount}
        </p>
      </div>
      {activeContent.type === "image" && (
        <ImagePlayer content={activeContent} switchContent={switchContent} />
      )}
      {activeContent.type === "video" && (
        <VideoPlayer content={activeContent} switchContent={switchContent} />
      )}
      {activeContent.type === "embed" && (
        <EmbedPlayer content={activeContent} switchContent={switchContent} />
      )}
      {activeContent.type === "text" && (
        <TextPlayer content={activeContent} switchContent={switchContent} />
      )}
    </main>
  );
}
