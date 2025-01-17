

import warnings

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import pairwise_distances

warnings.filterwarnings("ignore")

TAG = "K-MEANS-CLUST/ "


def get_initial_centroids(data, k, seed=None):
    
    rng = np.random.default_rng(seed)
    n = data.shape[0]  

    
    rand_indices = rng.integers(0, n, k)

    
    
    
    centroids = data[rand_indices, :]

    return centroids


def centroid_pairwise_dist(x, centroids):
    return pairwise_distances(x, centroids, metric="euclidean")


def assign_clusters(data, centroids):
    
    
    distances_from_centroids = centroid_pairwise_dist(data, centroids)

    
    
    cluster_assignment = np.argmin(distances_from_centroids, axis=1)

    return cluster_assignment


def revise_centroids(data, k, cluster_assignment):
    new_centroids = []
    for i in range(k):
        
        member_data_points = data[cluster_assignment == i]
        
        centroid = member_data_points.mean(axis=0)
        new_centroids.append(centroid)
    new_centroids = np.array(new_centroids)

    return new_centroids


def compute_heterogeneity(data, k, centroids, cluster_assignment):
    heterogeneity = 0.0
    for i in range(k):
        
        member_data_points = data[cluster_assignment == i, :]

        if member_data_points.shape[0] > 0:  
            
            distances = pairwise_distances(
                member_data_points, [centroids[i]], metric="euclidean"
            )
            squared_distances = distances**2
            heterogeneity += np.sum(squared_distances)

    return heterogeneity


def plot_heterogeneity(heterogeneity, k):
    plt.figure(figsize=(7, 4))
    plt.plot(heterogeneity, linewidth=4)
    plt.xlabel("# Iterations")
    plt.ylabel("Heterogeneity")
    plt.title(f"Heterogeneity of clustering over time, K={k:d}")
    plt.rcParams.update({"font.size": 16})
    plt.show()


def kmeans(
    data, k, initial_centroids, maxiter=500, record_heterogeneity=None, verbose=False
):
    
    centroids = initial_centroids[:]
    prev_cluster_assignment = None

    for itr in range(maxiter):
        if verbose:
            print(itr, end="")

        
        cluster_assignment = assign_clusters(data, centroids)

        
        
        centroids = revise_centroids(data, k, cluster_assignment)

        
        if (
            prev_cluster_assignment is not None
            and (prev_cluster_assignment == cluster_assignment).all()
        ):
            break

        
        if prev_cluster_assignment is not None:
            num_changed = np.sum(prev_cluster_assignment != cluster_assignment)
            if verbose:
                print(
                    f"    {num_changed:5d} elements changed their cluster assignment."
                )

        
        if record_heterogeneity is not None:
            
            score = compute_heterogeneity(data, k, centroids, cluster_assignment)
            record_heterogeneity.append(score)

        prev_cluster_assignment = cluster_assignment[:]

    return centroids, cluster_assignment



if False:  
    from sklearn import datasets as ds

    dataset = ds.load_iris()
    k = 3
    heterogeneity = []
    initial_centroids = get_initial_centroids(dataset["data"], k, seed=0)
    centroids, cluster_assignment = kmeans(
        dataset["data"],
        k,
        initial_centroids,
        maxiter=400,
        record_heterogeneity=heterogeneity,
        verbose=True,
    )
    plot_heterogeneity(heterogeneity, k)


def report_generator(
    predicted: pd.DataFrame, clustering_variables: np.ndarray, fill_missing_report=None
) -> pd.DataFrame:
    
    
    if fill_missing_report:
        predicted = predicted.fillna(value=fill_missing_report)
    predicted["dummy"] = 1
    numeric_cols = predicted.select_dtypes(np.number).columns
    report = (
        predicted.groupby(["Cluster"])[  
            numeric_cols
        ]  
        .agg(
            [
                ("sum", "sum"),
                ("mean_with_zeros", lambda x: np.mean(np.nan_to_num(x))),
                ("mean_without_zeros", lambda x: x.replace(0, np.nan).mean()),
                (
                    "mean_25-75",
                    lambda x: np.mean(
                        np.nan_to_num(
                            sorted(x)[
                                round(len(x) * 25 / 100) : round(len(x) * 75 / 100)
                            ]
                        )
                    ),
                ),
                ("mean_with_na", "mean"),
                ("min", lambda x: x.min()),
                ("5%", lambda x: x.quantile(0.05)),
                ("25%", lambda x: x.quantile(0.25)),
                ("50%", lambda x: x.quantile(0.50)),
                ("75%", lambda x: x.quantile(0.75)),
                ("95%", lambda x: x.quantile(0.95)),
                ("max", lambda x: x.max()),
                ("count", lambda x: x.count()),
                ("stdev", lambda x: x.std()),
                ("mode", lambda x: x.mode()[0]),
                ("median", lambda x: x.median()),
                ("# > 0", lambda x: (x > 0).sum()),
            ]
        )
        .T.reset_index()
        .rename(index=str, columns={"level_0": "Features", "level_1": "Type"})
    )  
    
    
    clustersize = report[
        (report["Features"] == "dummy") & (report["Type"] == "count")
    ].copy()
    
    clustersize.Type = "ClusterSize"
    clustersize.Features = "# of Customers"
    
    clusterproportion = pd.DataFrame(
        clustersize.iloc[:, 2:].to_numpy() / clustersize.iloc[:, 2:].to_numpy().sum()
    )
    
    clusterproportion["Type"] = "% of Customers"
    clusterproportion["Features"] = "ClusterProportion"
    cols = clusterproportion.columns.tolist()
    cols = cols[-2:] + cols[:-2]
    clusterproportion = clusterproportion[cols]  
    clusterproportion.columns = report.columns
    
    a = pd.DataFrame(
        abs(
            report[report["Type"] == "count"].iloc[:, 2:].to_numpy()
            - clustersize.iloc[:, 2:].to_numpy()
        )
    )
    a["Features"] = 0
    a["Type"] = "# of nan"
    
    a.Features = report[report["Type"] == "count"].Features.tolist()
    cols = a.columns.tolist()
    cols = cols[-2:] + cols[:-2]
    a = a[cols]  
    a.columns = report.columns  
    
    report = report.drop(report[report.Type == "count"].index)
    
    report = pd.concat([report, a, clustersize, clusterproportion], axis=0)
    report["Mark"] = report["Features"].isin(clustering_variables)
    cols = report.columns.tolist()
    cols = cols[0:2] + cols[-1:] + cols[2:-1]
    report = report[cols]
    sorter1 = {
        "ClusterSize": 9,
        "ClusterProportion": 8,
        "mean_with_zeros": 7,
        "mean_with_na": 6,
        "max": 5,
        "50%": 4,
        "min": 3,
        "25%": 2,
        "75%": 1,
        "# of nan": 0,
        "# > 0": -1,
        "sum_with_na": -2,
    }
    report = (
        report.assign(
            Sorter1=lambda x: x.Type.map(sorter1),
            Sorter2=lambda x: list(reversed(range(len(x)))),
        )
        .sort_values(["Sorter1", "Mark", "Sorter2"], ascending=False)
        .drop(["Sorter1", "Sorter2"], axis=1)
    )
    report.columns.name = ""
    report = report.reset_index()
    report = report.drop(columns=["index"])
    return report


if __name__ == "__main__":
    import doctest

    doctest.testmod()
