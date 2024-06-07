"use client";

import Image from "next/image";
import { FiAirplay } from "react-icons/fi";
import { TbFaceId, TbFaceIdError } from "react-icons/tb";
import { useEffect, useState } from "react";
import axios from "axios";
import CustomLoader from "@/components/CustomLoader";

export default function Home() {
  const [screens, setScreens] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchScreens = async () => {
    try {
      const res = await axios({
        method: "GET",
        url: `${process.env.NEXT_PUBLIC_API_URL}/screens/`,
        withCredentials: true,
      });
      setScreens(res.data);
    } catch (error) {
      console.error(error);
      setError(error);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchScreens();
  }, []);

  if (loading) {
    return (
      <main className="flex min-h-screen flex-col items-center justify-center">
        <CustomLoader />
      </main>
    );
  }

  return (
    <main className="flex min-h-screen flex-col items-center relative">
      <section className="w-full p-6 relative mb-28">
        <div className="w-full flex flex-col items-center justify-center p-8 min-h-[350px] rounded-3xl shadow-lg bg-[url('/img/hero-bg.png')] bg-center bg-cover bg-no-repeat">
          <h2 className="text-[45px] text-sky-500 text-center font-[500]">
            What&apos;s New on Campus
          </h2>
          <p className="text-[16px] text-gray-700 text-center">
            Stay informed and inspired with the latest news and announcements
          </p>
          <div className="flex items-center bg-gray-100 p-2 px-4 rounded-full mt-8">
            <FiAirplay className="w-6 h-6 text-gray-600 mr-2" />
            <h1 className="text-md font-[400] text-gray-700">1337 Signage</h1>
          </div>
        </div>
      </section>

      <section className="flex flex-col items-center justify-center gap-8 mt-2 w-[94%] md:w-10/12 mb-16">
        <div className="flex flex-col items-center w-full pm-4">
          <h1 className="text-center font-semibold text-xl text-sky-400">
            Explore all Screens
          </h1>
          <svg
            aria-hidden="true"
            viewBox="0 0 418 42"
            preserveAspectRatio="none"
            className="w-[220px] mt-2"
            fill="#0ea5e9"
          >
            <path d="M203.371.916c-26.013-2.078-76.686 1.963-124.73 9.946L67.3 12.749C35.421 18.062 18.2 21.766 6.004 25.934 1.244 27.561.828 27.778.874 28.61c.07 1.214.828 1.121 9.595-1.176 9.072-2.377 17.15-3.92 39.246-7.496C123.565 7.986 157.869 4.492 195.942 5.046c7.461.108 19.25 1.696 19.17 2.582-.107 1.183-7.874 4.31-25.75 10.366-21.992 7.45-35.43 12.534-36.701 13.884-2.173 2.308-.202 4.407 4.442 4.734 2.654.187 3.263.157 15.593-.78 35.401-2.686 57.944-3.488 88.365-3.143 46.327.526 75.721 2.23 130.788 7.584 19.787 1.924 20.814 1.98 24.557 1.332l.066-.011c1.201-.203 1.53-1.825.399-2.335-2.911-1.31-4.893-1.604-22.048-3.261-57.509-5.556-87.871-7.36-132.059-7.842-23.239-.254-33.617-.116-50.627.674-11.629.54-42.371 2.494-46.696 2.967-2.359.259 8.133-3.625 26.504-9.81 23.239-7.825 27.934-10.149 28.304-14.005.417-4.348-3.529-6-16.878-7.066Z"></path>
          </svg>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-8 w-full my-4">
          {screens?.length > 0 &&
            screens.map((screen) => (
              <a
                className="flex justify-center items-center cursor-pointer w-full rounded-xl hover:shadow-xl transition-all duration-300 ease-in-out"
                href={`/screens/${screen.id}`}
                key={screen.id}
              >
                <div className="relative  w-full h-48 rounded-xl">
                  <div className="absolute inset-0 border-2 border-gray-200 rounded-xl backdrop-blur-md z-10">
                    <div className="flex justify-center items-center w-full h-full ">
                      <h1 className="text-md font-semibold text-gray-600 text-transform: capitalize">
                        {screen.name}
                      </h1>
                    </div>
                  </div>
                  <div className="w-full bg-[url('/img/hero-bg.png')] bg-left bg-no-repeat absolute h-full z-1 rounded-xl"></div>
                  <div className="absolute -bottom-2 left-1/2 transform -translate-x-1/2 bg-gray-500 w-16 h-2 rounded-b-lg"></div>
                </div>
              </a>
            ))}
        </div>
        <div className="w-full flex justify-center">
          {screens?.length === 0 && (
            <div className="flex items-center justify-center gap-2 bg-gray-100 px-4 py-2 rounded-md">
              <TbFaceId className="w-8 h-8 text-gray-500" />
              <p className="text-gray-500 text-[14px]">No screens available</p>
            </div>
          )}
          {error && (
            <div className="flex flex-col items-center justify-center">
              <div className="flex items-center justify-center gap-2 bg-red-100 px-4 py-2 rounded-md">
                <TbFaceIdError className="w-8 h-8 text-red-500" />
                <p className="text-red-500 text-[14px]">
                  Error fetching screens. Please try again later
                </p>
              </div>
              <a
                href="/"
                className="text-blue-500 text-[14px] underline underline-offset-2 mt-2 cursor-pointer"
              >
                Refresh
              </a>
            </div>
          )}
        </div>
      </section>
      <footer className="w-full bg-gray-100 p-4 mt-24 absolute bottom-0">
        <p className="text-center text-gray-600 text-[13px]">
          &copy; {new Date().getFullYear()} 1337 Signage. All rights reserved.
        </p>
      </footer>
    </main>
  );
}
