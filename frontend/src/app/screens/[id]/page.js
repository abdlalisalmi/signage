"use client";

import { useEffect, useState } from "react";
import axios from "axios";
import { PiScreencastFill } from "react-icons/pi";
import Image from "next/image";
import { getMediaAbsolutePath, removeDuplicates } from "@/utils";
import Layout from "@/components/Layout";
import ContentsPlayer from "@/components/contentPlayers/ContentsPlayer";
import EmptyContents from "@/components/contentPlayers/EmptyContents";

export default function ScreenPlay({ params }) {
  const [loading, setLoading] = useState(true);
  const [screenData, setScreenData] = useState(null);
  const [error, setError] = useState(null);
  const [contents, setContents] = useState([]);

  const fetchScreenDetails = async () => {
    try {
      const res = await axios({
        method: "GET",
        url: `${process.env.NEXT_PUBLIC_API_URL}/screens/${params.id}/`,
        withCredentials: true,
      });
      setScreenData(res.data);
      if (res.data.playlists) {
        let conts = [];
        res.data.playlists.map((playlist) => {
          conts = [...conts, ...playlist.contents];
        });
        conts = removeDuplicates(conts, "id");
        setContents(conts);
      }
    } catch (error) {
      setError(error);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchScreenDetails();
  }, []);

  return (
    <Layout error={error} loading={loading}>
      {contents.length === 0 ? (
        <EmptyContents />
      ) : (
        <ContentsPlayer initialContents={contents} />
      )}
    </Layout>
  );
}
