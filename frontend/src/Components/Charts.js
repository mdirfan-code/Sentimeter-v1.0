import React, { useEffect, useState } from "react";
import { getTweetData } from "../Adapters/analysis";
import { Doughnut } from "react-chartjs-2";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import Highcharts from "highcharts";
import HighchartsReact from "highcharts-react-official";
import HC_more from "highcharts/highcharts-more";

HC_more(Highcharts);

ChartJS.register(ArcElement, Tooltip, Legend);

function Charts({ search }) {
  const [sentimentData, setSentimentData] = useState({});
  const [donutData, setDonutData] = useState({
    labels: ["positive", "negative", "neutral"],
    datasets: [
      {
        label: "# of Votes",
        data: [10, 20, 30],
        backgroundColor: [
          "rgba(255, 99, 132, 0.5)",
          "rgba(54, 162, 235, 0.5)",
          "rgba(255, 206, 86, 0.5)",
        ],
        borderColor: [
          "rgba(255, 99, 132, 1)",
          "rgba(54, 162, 235, 1)",
          "rgba(255, 206, 86, 1)",
        ],
        borderWidth: 1,
      },
    ],
  });
  const [freqData, setFreqData] = useState({
    chart: {
      type: "packedbubble",
      height: "50%",
    },
    title: {
      text: "Word Patterns",
    },
    tooltip: {
      useHTML: true,
      pointFormat: "<b>{point.name}:</b> {point.value}",
    },
    plotOptions: {
      packedbubble: {
        minSize: "10%",
        maxSize: "200%",
        zMin: 0,
        zMax: 50,
        layoutAlgorithm: {
          splitSeries: false,
          gravitationalConstant: 0.02,
        },
        dataLabels: {
          enabled: true,
          format: "{point.name}",
          filter: {
            property: "y",
            operator: ">",
            value: 1,
          },
          style: {
            color: "black",
            textOutline: "none",
            fontWeight: "normal",
          },
        },
      },
    },

    series: [
      {
        name: "Data",
        data: [
          { name: "Work", value: 200 },
          { name: "Jeff", value: 50 },
          { name: "Neil", value: 10 },
          { name: "rain", value: 5 },
          { name: "meeting", value: 3 },
        ],
      },
    ],
  });
  useEffect(() => {
    const fetchData = async () => {
      const res = await getTweetData(search);
      console.log(res);
      if (res.data.success === 0) {
        return;
      }
      setSentimentData(res.data.result);
      const series = [
        {
          name: "Data",
          data: res.freq,
        },
      ];
      setFreqData({ ...freqData, series });
      console.log([
        sentimentData.Positive,
        sentimentData.Negative,
        sentimentData.Nuteral,
      ]);
      const data = {
        ...donutData,
        datasets: [
          {
            label: "Sentiment",
            data: [
              res.data.result.Positive,
              res.data.result.Negative,
              res.data.result.Nuteral,
            ],
            backgroundColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
            ],
            borderWidth: 1,
          },
        ],
      };
      setDonutData(data);
    };
    fetchData();
  }, []);

  return (
    <div className="chart-container">
      <div className="donut">
        <Doughnut data={donutData} />
      </div>
      <div className="bubble">
        <HighchartsReact highcharts={Highcharts} options={freqData} />
      </div>
    </div>
  );
}

export default Charts;
