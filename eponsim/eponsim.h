/*
	TITLE: 		EPON Simulator Definitions
	AUTHOR: 	Michael P. McGarry
	DATE:
	VERSION:	1.0
	
	NOTES:
	
*/

#ifndef EPONSIM_H
#define EPONSIM_H

#include <csim.h>

/*
 * Macro definitions
 */
double			maximumGrantCycle;
#define MAX(A,B) ((A) > (B) ? (A):(B))
#define MIN(A,B) ((A) < (B) ? (A):(B))

#ifdef DEBUG_TRC_HI
#define DEBUG_TRC
#define DEBUG_TRC_LO
#endif

#ifdef DEBUG_TRC
#define DEBUG_TRC_LO
#endif

#ifdef DEBUG_ONU
#define DEBUG_ONU
#endif

#define MAX_SS_SIM_TIME	4000

#define CI_HALFWIDTH_PERCENTAGE	0.8

/* Preamble/IPG in bytes */
#define PREAMBLE_IPG_BYTES  20     /* 7-byte preamble, 1-byte SFD, and 12-byte IPG */

/* Maximum ONU buffer size before halting simulation */
#define MAX_PKT_BUF_SIZE	2e9
// #define MAX_PKT_BUF_SIZE	2e15

/* Maximum FATAL Error allowed before halting simulation */
#define	MAX_FATAL_ERRORS	1

/* FATAL Error Codes */
#define FATAL_CAUSE_BUFFER_OVR		0
#define FATAL_CAUSE_MAC_CONTENTION	1
#define FATAL_CAUSE_STRAY_PKT		2
#define FATAL_CAUSE_INV_WA		3
#define FATAL_CAUSE_GATE_TOO_SMALL  	4
#define FATAL_CAUSE_NO_GRANT		5
#define FATAL_CAUSE_NO_MEM		6
#define FATAL_CAUSE_MISC		10
#define FATAL_CAUSE_LENGTH_VIDEO_BUFFER_OVR		20
#define FATAL_CAUSE_LENGTH_DATA_BUFFER_OVR		21

#define MAX_ONU		64
#define	MAX_LAMBDAS	64

/* Maximum size of trace capability */
#define MAX_TRACE_VALUES    1500

/* constants for NULL values */
#define ONU_NULL	-1
#define LAMBDA_NULL	-1

/* Lambda Map constants */
#define LAMBDA_TRUE     1
#define LAMBDA_FALSE    0

/* Fixed Propagation Delay definitions */
#define FIXED_PROP_DELAY_OFF	0
#define FIXED_PROP_DELAY_ON	    1

/* Simulation Trace definitions */
#define SIM_TRACE_OFF	0
#define SIM_TRACE_ON	1

/* Video Queue Service definitions */
#define NOT_SERVICED	0
#define SERVICED	1

/* Grant Trace definitions */
#define GRANT_TRACE_OFF	0
#define GRANT_TRACE_ON	1
#define GRANT_TRACE_SIZE    1000

/* Get Tail definitions */
#define GET_TAIL_OFF	0
#define GET_TAIL_ON	    1

/* OLT Type definitions */
#define OLT_IPACT						0
#define OLT_WDM_IPACT		 	        1
#define OLT_LEAST_ASSIGNED	 	        2
#define OLT_APS							3
#define OLT_LFJ				 			4
#define OLT_LFJ_LPT			 			7
#define OLT_LFJ_SPT			 			8
#define OLT_WBM                         9
#define OLT_ONLINE_NASC		         	5
#define OLT_ONLINE_INTERVAL_LFJ_LPT	 	6
#define OLT_ONLINE_INTERVAL_LFJ_SPT		10
#define OLT_ONLINE_INTERVAL_WBM			11
#define OLT_ONLINE_JIT_LFJ_LPT	        12
#define OLT_ONLINE_JIT_LFJ_SPT	        13
#define OLT_ONLINE_JIT_WBM				14
#define OLT_ONLINE_JIT_LFJ_LNF	        15
#define OLT_ONLINE_JIT_WBM_LPT	        16
#define OLT_ONLINE_JIT_WBM_LNF	        17
#define OLT_ONLINE_INTERVAL_LFJ_LNF		18
#define OLT_ONLINE_INTERVAL_WBM_LPT		19
#define OLT_ONLINE_INTERVAL_WBM_LNF		20
#define OLT_EAF                         21
#define OLT_EAAF                        22
#define OLT_ONLINE_INTERVAL_EAF         23
#define OLT_ONLINE_INTERVAL_EAAF        24
#define OLT_ONLINE_JIT_EAF              25
#define OLT_ONLINE_JIT_EAAF             26
#define OLT_ONLINE_JIT_WBM_EAAF         27
#define OLT_ONLINE_INTERVAL_WBM_EAAF    28
#define OLT_ONLINE_JIT_TEST             30
#define OLT_LFJ_LNF                     31
#define OLT_WBM_LPT                     32
#define OLT_WBM_LNF                     33
#define OLT_WBM_EAAF                    34
#define OLT_SPD                         40
#define OLT_LPD                         41
#define OLT_SPD_LPT                     42
#define OLT_ONLINE_JIT_SPD              43
#define OLT_ONLINE_JIT_LPD              44
#define OLT_IPACT_PSF					45

/* DBA Type definitions */
#define DBA_FIXED				0
#define DBA_LIMITED_GATE		1
#define DBA_LIMITED_CYCLE		2
#define DBA_GATED				3
#define DBA_CONSTANT_CREDIT		4
#define DBA_LINEAR_CREDIT		5
#define DBA_ELASTIC				6
#define DBA_EXCESS     			7

/* Video DBA Type definitions */

#define VIDEO_DBA_FIXED				0
#define VIDEO_DBA_LIMITED_GATE		1
#define VIDEO_DBA_GATED				2

/* Traffic Type definitions */
#define TRAFFIC_POISSON				0
#define TRAFFIC_SELF_SIMILAR		1

/* Video Traffic Flag Values */
#define VIDEO_TRAFFIC_OFF		0
#define VIDEO_TRAFFIC_ON		1
#define VIDEO_PREDICTION_OFF	0
#define VIDEO_PREDICTION_ON		1

#define SCALABLE_VIDEO_OFF		0
#define SCALABLE_VIDEO_ON		1
#define SCALABLE_VIDEO_DROPPING_OFF			0
#define SCALABLE_VIDEO_DROPPING_THRESHOLD	1
#define SCALABLE_VIDEO_DROPPING_DYNAMIC		2
#define SCALABLE_VIDEO_DROPPING_LINEAR_THRESHOLD	3

/* WDM Type definitions */
#define	WDM_NONE	0
#define	WDM_FIXED	1
#define	WDM_TUNABLE	2

#define AVG_PKT_SIZE	493.7

/* ONU Scheduling Pool States */
#define ONU_SCHED_INACTIVE  0
#define ONU_SCHED_ACTIVE    1
#define ONU_SCHED_IMMINENT  2

/* Optimization Scheduler definitions */
#define COST_INFINITE			(MAXINT/2)
#define COST_WAVELENGTH_SWITCH		100
#define	COST_TSLOT_PENALTY		10
#define COST_DUMMY			((COST_INFINITE) - 1)

#define MAX_SCHEDULER_NUM_SLOT		1000

/*
 * Some useful macros
 */
/* Setup lambda free temp data structure */
#define mSETUP_TEMP_LAMBDA_FREE(loopVar) \
    do { \
    for(loopVar = 0; loopVar < simParams.NUM_LAMBDAS; loopVar++) \
    { \
        lambdaFreeTemp[loopVar] = lambdaFree[loopVar]; \
    } } while(0)
/* Update lambda free array to current sim time */
#define mUPDATE_LAMBDA_FREE(loopVar,lambdaFreeArray) \
    do { \
    for(loopVar = 0; loopVar < simParams.NUM_LAMBDAS; loopVar++) \
    { \
        if(lambdaFreeArray[loopVar] < simtime()) \
        { \
            lambdaFreeArray[loopVar] = simtime(); \
        } \
    } } while(0)
    
    
double	remainingVideoGrantLength;
double	maximumGrantCycle;


/*
 * Type definitions
 */

typedef struct
{
	/* parameters directly set */
	int		OLT_TYPE;
	int		DBA_TYPE;
	int		VIDEO_DBA_TYPE;
	int		TRAFFIC_TYPE;
	int		WDM_TYPE;
	int		NUM_RUNS;       	/* Number of independent runs */
	int		NUM_LAMBDAS;		/* Number of wavelengths supported on PON */
	int		NUM_ONU;		/* Number of ONUs on PON */
	int		NUM_HEAVY_ONU;		/* Number of heavily loaded ONUs */
	int		NUM_WDM_ONU;		/* Number of WDM ONUs */
	int		NUM_UH_WDM_ONU;		/* Number of Upper Half WDM ONUs */
	int		NUM_LH_WDM_ONU;		/* Number of Lower Half WDM ONUs */
	int		NUM_PREFERRED_ONU;	/* Number of Preferrentially Treated ONUs */
	int		NUM_SS_STREAMS;		/* Number of Self Similar Traffic Generator Streams */
	double		SS_HURST_PARAM;		/* Hurst Parameter for Self-Similar Traffic Generator */
	double		LINK_SPEED;		/* link speed in bps */
	double		DESIRED_LOAD;		/* desired traffic load */
	double		PIPG_LOAD;		/* traffic load with Preamble/IPG */
	int		HEAVY_LOAD;     	/* heavy load (measured in number of times greater than a lightly loaded ONU) */
	double		GUARD_TIME;		/* guard time between grants */
	double		TUNING_TIME;		/* tuning time for tunable lasers */
	double		SIM_TIME;       	/* total simulation time */
	double		START_LOAD;
	double		END_LOAD;
	double		LOAD_INCR;
	int		START_LAMBDA;
	int		END_LAMBDA;
	long		RAND_SEED;
	double		SIM_TRACE_TIMESCALE;
    	double		SIM_TRACE_TIME;
	int		SIM_TRACE;
	int		GRANT_TRACE;
	int		GET_TAIL;		/* Get tails for histogram (each simulation will run twice!!!) */
	
	/* parameters calculated from specified parameters */
	int	NUM_PARTS;		/* Number of bandwidth partitions */
	double	LINK_SPEED_PER_PART;	/* in bps */
	double	AVG_PKT_INTER_ARVL_TIME;
	double	AVG_PKT_INTER_ARVL_TIME_HEAVY;
	double	TIME_PER_BYTE;
	double	PREAMBLE_IPG_TIME;
	/* Self Similar Traffic Generator Parameters */
	double	SS_PARETO_LOC_PARAM;
	double	SS_OFF_LOC_PARAM;
	double	SS_OFF_LOC_PARAM_HEAVY;
	double	SS_PARETO_SHAPE_PARAM;
	
	/* Video Traffic Generator Parameters */
	char	VIDEO_TRAFFIC;			/* Flag indicating whether video traffic generators are used for all ONUs */
	char 	VIDEO_PREDICTION;
	double 	FRAME_RATE;
	double	TIME_SHIFT;
	char	PREDICTION_TYPE[10];
	char 	VIDEO_TRACE_FILE[200];		/* Video trace file name */
	
	char	SCALABLE_VIDEO_TRAFFIC;
	char	SCALABLE_VIDEO_DROPPING_ALGORITHM;
	char	SCALABLE_VIDEO_NUM_LAYERS;
	char	SV_DROP_LAYER_THRESHOLD;
	double	SV_DROP_SENSITIVITY;
	int		SV_DROP_NUM_VALUES_FOR_MA;
	double	SV_DROP_MIN_BOUND;
	double	SV_DROP_MAX_BOUND;
	
	//double	LINK_SPEED_PER_SS_STREAM;
	double		AVG_BURST_SIZE;
	double		AVG_T_ON;
	double		AVG_T_OFF;
	double		AVG_T_OFF_HEAVY;
	/* OLT Scheduler Parameters */
	double		SCHEDULE_INTERVAL;		/* Online Scheduler: Scheduling Wait Interval */
	int		FIXED_GRANT_SIZE;		/* DBA Fixed Grant Size */
	int		MAX_GRANT_SIZE;			/* DBA Maximum Grant Size */
	int		SCHEDULER_MAX_WINDOW;		/* Maximum Window Flag */
	int		SCHEDULER_NUM_SLOT;		/* Number of Slots in Schedule Window */
	int		SCHEDULER_SLOT_SIZE;		/* Slot Size */
	int		STARVE_THRESH;			/* Starvation Threshold for JIT schedulers (in scheduling rounds) */
	int		FIXED_PROP_DELAY;
	double		FIXED_PROP_DELAY_VALUE;
	double		MAX_PROP_DELAY;
	double		ACTUAL_MAX_PROP_DELAY;
	double		ACTUAL_MIN_PROP_DELAY;
	double		SHORTEST_POLL_TIME;
	double		AVAIL_COST_WEIGHT;		/* Availability Cost weight for WBM schedulers */

	double		ONU_PROP[MAX_ONU];		/* ONU to OLT propagation delay values */
	
} sSIM_PARAMS;

/* Packet entity data structure */
typedef struct entity_pkt
{
	double	creationTime;
	double	transmissionTime;
	double	arrivalTime;
	int	size;
	/* Rami will add fields relevant to video packets */
	/*  int		type; */
	char	frameType;
	int	forecastSize;
	double	frameTimeStamp;
	int	forecastPktNumber;
	int layer;
	
	struct	entity_pkt *next;
} sENTITY_PKT;

/* GATE entity data structure */
typedef struct entity_gate_pkt
{
	double	start;		/* GATE start in time */
	double	length;		/* GATE total length in time */
	double	data_length;	/* GATE data length in time */
	double	video_length;	/* GATE video length in time */
	double	grant;		/* GATE total length in bytes */
	double	data_grant;	/* GATE data length in bytes */
	double	video_grant;	/* GATE video length in bytes */
	int	lambda; 	/* Assigned length */
} sENTITY_GATE_PKT;

/* ONU attribute structure */
typedef struct
{
	sENTITY_PKT		*packetsHead;
	sENTITY_PKT		*packetsTail;
	double				packetQueueSize;	/* Packet Queue Size (in bytes) */
	unsigned long		packetQueueNum;		/* # of Packets in Queue */
	double 			rptQueueSize;		/* Reported Queue Size (in bytes) */
	unsigned long		rptQueueNum;		/* # of Reported packets in Queue */
	sENTITY_PKT		*packetsVideoHead;
	sENTITY_PKT		*packetsVideoTail;
//	unsigned long		packetVideoQueueSize;	/* Packet Video Queue Size (in bytes) */
	double				packetVideoQueueSize;	/* Packet Video Queue Size (in bytes) */
	unsigned long		packetVideoQueueNum;	/* # of Packets in Video Queue */
//	unsigned long		packetForecastVideoQueueSize;
	double				packetForecastVideoQueueSize;
	unsigned long		packetForecastVideoQueueNum;
	double				packetForecastVideoTime;
// 	unsigned long		rptVideoQueueSize;	/* Reported Video Queue Size (in bytes) */
	double				rptVideoQueueSize;	/* Reported Video Queue Size (in bytes) */
	unsigned long		rptVideoQueueNum;	/* # of Reported packets in Video Queue */
//	unsigned long		rptForecastVideoQueueSize;
	double				rptForecastVideoQueueSize;
	unsigned long		rptForecastVideoQueueNum;
	double			rptForecastVideoTime;
	double			previousGrantStartTime;
	double			startoffset;
	double			startFrame;
	double			maxFrameCount;
	double			sentFrameCount;
	double			currentFrame;
	double			wrapAround;
	double			averageGrantCycle;
	double			totalNumberGrantCycle;
	double			maximumGrantCycle;
	double			maximumGrantCycleTime;
//	unsigned long		remainPSFgrant;		
//	unsigned long		grantLen;		/* current Grant Length (in bytes) */
//	unsigned long		dataGrantLen;		/* current Data Grant Length (in bytes) */
//	unsigned long		videoGrantLen;		/* current Video Grant Length (in bytes) */
	double				remainPSFgrant;		
	double				grantLen;		/* current Grant Length (in bytes) */
	double				dataGrantLen;		/* current Data Grant Length (in bytes) */
	double				videoGrantLen;		/* current Video Grant Length (in bytes) */
	int			videoServiced;
	double 			rptTime;		/* time of latest REPORT */
	double			prevGateTime;		/* time of previous GATE */
	double			readyTime;		/* time ONU is ready for scheduling (i.e., after REPORT transmission) */
	int			step2Sched;		/* flag to indicate whether ONU is scheduled in step 2, used by Online JIT */
	double 			minArrivalTime;		/* Minimum arrival time in Queue */
	double			avgArrivalTime;		/* Average arrival time in Queue */
	double 			minArrivalTimeVideo;		/* Minimum arrival time in Queue */
	double			avgArrivalTimeVideo;		/* Average arrival time in Queue */	
	MBOX			grantMailbox[MAX_LAMBDAS];
	MBOX			pktMailbox;
	double			latency;
	double			rtt;
	int			supportedLambdas[MAX_LAMBDAS+1];	/* List of supported lambdas, terminated with LAMBDA_NULL */
	int			supportedLambdasMap[MAX_LAMBDAS];	/* Supported Lambdas Map */
	int			numSupportedLambdas;
	int			tunedLambda;
	int			wdmType;
	double			tuningTime;
	int			priority;
	int			tslotStart;
	TABLE			transmitTimeTable;
	TABLE			transmitVideoTimeTable;
	TABLE			queueTimeTable;
	TABLE			VideoqueueTimeTable;
	TABLE			queueLengthTable;
    	METER			zeroReqRate;
    	METER			nonzeroReqRate;
	STREAM			pktInterArrivalStream;
	STREAM			pktSizeStream;
	STREAM			burstSizeStream;
//	unsigned long		transmitByteCnt;
//	unsigned long		transmitVideoByteCnt;
	double				transmitByteCnt;
	double				transmitVideoByteCnt;
	TABLE			transmitThroughput;
} sONU;

/* Scheduling Pool Data Structure */
typedef struct
{
    int     state;      /* ONU activity state (2 - imminent, 1 - in scheduling pool, 0 - inactive) */
    double  poolTime;   /* simulation time entered pool */
    int     gateLambda; /* scheduled lambda */
    double  gateStart;  /* scheduled start */
    double  gateLength; /* scheduled length */
    int     rounds;     /* age in scheduling rounds */
    /*
    numLambda - number of supported wavelengths [can get from onuAttrs]
    grantSize[NUM_CLASSES] - grant size for traffic class X
    */
} sSCHED_POOL;

typedef struct
{
	double			estimatedMean;
	double			intervalLower;
	double			intervalUpper;
	unsigned long		insideIntervalCount;
	unsigned long		outsideIntervalCount;
	double			confidenceLevel;
} sSS_STAT;

/* Statistic Estimation Structure */
typedef struct
{
    double  meanEst;
    double  minEst;
    double  maxEst;
} sSTAT_EST;

typedef enum
{
	PILOT_RUN,
	ACTUAL_RUN,
	TAIL_RUN,
	TIME_TRACE
} eSIM_TYPE;

eSIM_TYPE simType;

typedef struct
{
    int     onuNum;
    double  startTime;
    double  length;
} sGRANT_TRC;

/* 
 * Integer Linked List structure
 */
struct onu_list
{
	int		onuNum;
	int		posNum;
	unsigned long  grantLen;	/* in bytes */
	unsigned long  numFrames;	/* in frames */
	double          grantTime;	/* in seconds */
	double          poolTime;	/* in seconds */
	double          minArrivalTime;	/* in seconds */
	double          avgArrivalTime;	/* in seconds */
	double		latency;	/* in seconds */
	struct onu_list *next;
};
typedef struct onu_list sONU_LIST;

typedef enum {SORT_ASCENDING_ORDER, SORT_DESCENDING_ORDER} eSORT_METHOD;

typedef enum {SORT_ONU_NUM, SORT_POS_NUM, SORT_GRANT_LEN, SORT_NUM_FRAMES, SORT_GRANT_TIME, SORT_POOL_TIME, SORT_MIN_ARRIVAL, SORT_AVG_ARRIVAL, SORT_PROP_DELAY} eSORT_CRITERIA;

typedef enum {SORT_EQ, SORT_GT, SORT_LT} eSORT_EQUAL;

/*
 * Global variable declarations
 */
extern char procId[20];

/* simulation parameters data structure */
extern sSIM_PARAMS simParams;

/* ONU attributes structure array */
extern sONU onuAttrs[MAX_ONU];

/* a flag to signal a graceful termination of the simulation */
extern int terminateSim;
extern int simInitPhase;

/* count of fatal errors in the simulation */
extern int fatalErrorCount;
extern int fatalErrorCode;

/* Trace messaging buffers */
extern char sim_msg_buf[10000];
extern char dump_msg_buf[1000];

/*
 * Grant Trace Data Structures
 */
extern sGRANT_TRC grantTrace[MAX_LAMBDAS][GRANT_TRACE_SIZE];
extern int grantTracePtr[MAX_LAMBDAS];

/* Empirical Packet Size Distribution */
#define EMPIRICAL_SIZE	4
extern double	EMPIRICAL_PROB[5];
extern double	EMPIRICAL_VALUE[5];
extern double	EMPIRICAL_CUTOFF[5];
extern long	EMPIRICAL_ALIAS[5];

/* CSIM Data Collection Variables */
extern TABLE		overallQueueDelay;
extern TABLE		queueDelay;

extern TABLE		overallVideoQueueDelay;
extern TABLE		overallVideoQueueDelay_MovingAverage;
extern TABLE		unusedVideoGrant;
extern TABLE		videoReport;
extern TABLE		VideoqueueDelay;
extern TABLE		cycleVideoQueueDelay;

extern TABLE		cycleQueueDelay;
extern TABLE		heavyQueueDelay;
extern TABLE		lightQueueDelay;
extern TABLE		preferQueueDelay;
extern TABLE		overallQueueLength;
extern TABLE		heavyQueueLength;
extern TABLE		lightQueueLength;
extern TABLE		preferQueueLength;

extern TABLE		overallGrantSize;
extern TABLE		overallGrantSizePkt;
extern TABLE		heavyGrantSize;
extern TABLE		lightGrantSize;
extern TABLE		overallCycleLength;
extern TABLE		heavyCycleLength;
extern TABLE		lightCycleLength;
extern TABLE		preferCycleLength;
extern TABLE		overallRptToSchedTime;
extern TABLE		heavyRptToSchedTime;
extern TABLE		lightRptToSchedTime;
extern TABLE		overallRptToGateTime;
extern TABLE		heavyRptToGateTime;
extern TABLE		lightRptToGateTime;
extern TABLE		numONUSched;
extern TABLE		loadBalanceMeasure;
extern TABLE		schedRounds;

extern TABLE		compRatio1;
extern TABLE		compRatio2;
extern TABLE		minCompRatio;

extern TABLE		excessBandwidth;
extern TABLE		excessBandwidthONU;

extern METER		overallGrantRate;
extern METER		heavyGrantRate;
extern METER		lightGrantRate;
extern METER		overallZeroReqRate;
extern METER		heavyZeroReqRate;
extern METER		lightZeroReqRate;
extern METER		overallNonzeroReqRate;
extern METER		heavyNonzeroReqRate;
extern METER		lightNonzeroReqRate;

extern sSTAT_EST	overallQueueDelayEst;
extern sSTAT_EST	heavyQueueDelayEst;
extern sSTAT_EST	lightQueueDelayEst;
extern sSTAT_EST	overallQueueLengthEst;
extern sSTAT_EST	heavyQueueLengthEst;
extern sSTAT_EST	lightQueueLengthEst;
extern sSTAT_EST	overallGrantSizeEst;
extern sSTAT_EST	overallGrantSizePktEst;
extern sSTAT_EST	heavyGrantSizeEst;
extern sSTAT_EST	lightGrantSizeEst;
extern sSTAT_EST	overallCycleLengthEst;
extern sSTAT_EST	heavyCycleLengthEst;
extern sSTAT_EST	lightCycleLengthEst;
extern sSTAT_EST	overallRptToSchedTimeEst;
extern sSTAT_EST	heavyRptToSchedTimeEst;
extern sSTAT_EST	lightRptToSchedTimeEst;
extern sSTAT_EST	overallRptToGateTimeEst;
extern sSTAT_EST	heavyRptToGateTimeEst;
extern sSTAT_EST	lightRptToGateTimeEst;
extern sSTAT_EST	numONUSchedEst;

extern sSS_STAT		overallQueueDelayStat;
extern sSS_STAT		heavyQueueDelayStat;
extern sSS_STAT		lightQueueDelayStat;
extern sSS_STAT		overallQueueLengthStat;
extern sSS_STAT		heavyQueueLengthStat;
extern sSS_STAT		lightQueueLengthStat;

/* Reset throughput flag */
extern int		reset_throughput_flag;
/* Throughput Fairness data structures */
extern double		actual_tput[MAX_ONU];
extern double		ideal_tput[MAX_ONU];
extern TABLE		throughputFairness;

/* Structures used for sorting ONUs */
/* This array is used for ordering ONUs for scheduling in LFJ order or in wavelength assignment order */
extern sONU_LIST *scheduleList[MAX_LAMBDAS];
extern sONU_LIST *scheduleListLfjSpt[MAX_LAMBDAS];
extern sONU_LIST *scheduleListLfjLpt[MAX_LAMBDAS];
#ifdef DEBUG_TRC_LO
extern sONU_LIST *trcList[MAX_LAMBDAS];
#endif
/* Scheduling Pool structure array */
extern			sSCHED_POOL schedPool[MAX_ONU];
extern int schedPoolCount;

/* Structures used for managing multiple wavelengths */
extern FACILITY lambda[MAX_LAMBDAS];		/* each wavelength is modeled as a facility */

extern double	lambdaFree[MAX_LAMBDAS];	/* array to keep track of lambda free times */
extern double	lambdaFreeTemp[MAX_LAMBDAS];	/* array to keep track of lambda free times (temp version) */

extern double 	downstreamFree;			/* keeps track of availability of downstream channel (assumes only GATE messages) */

extern int		lambdaAssign[MAX_LAMBDAS];	/* array to keep track of lambda ONU assignments */


/*
 * Function declarations
 */
/* Sim core dump */
void dump_sim_core();

/*----------------David's Troubleshooting----------------*/

// Enable printing to a structured file
#define EnableTroubleshooting_v1	1

// Enable printing to a sequential file
#define EnableTroubleshooting_v2	1

// Enable printing of process statuses
// #define EnableTroubleshooting_v3	1

// Enable ONU printing
// #define EnableTroubleshooting_v4	1

// Define Test Variable Types
typedef struct
{
	double	main_start,
			main_finish,
			read_sim_cfg_file_start,
			read_sim_cfg_file_finish,
			heartbeat_process,
			// That's [run# (probably only 1)][load level (probably 0.1 to 0.9)][PilotRun == 0, ActualRun == 1]
			main_begin_lambda[10],
			main_end_lambda[10],
			main_test[10][20],
			main_begin_load[10][20],
			main_end_load[10][20],
			gate_created[10][20],
			gate_destroyed[10][20],
			sim_start[10][20][2],
			sim_process[10][20][2],
			sim_before_ONU_processes[10][20][2],
			sim_finish[10][20][2],
			sim_finish2[10][20][2],
			sim_ctrl_simType[10][20][2],
			sim_ctrl_videoTraffic[10][20][2],
			sim_ctrl_testProbe[10][20][2],
			traffic_src_video_start[10][20][64],
			traffic_src_video_process[10][20][64],
			traffic_src_video_finish[10][20][64],
			traffic_scalable_video_start[10][20][64],
			traffic_scalable_video_process[10][20][64],
			traffic_scalable_video_finish[10][20][64],
			vid_pkt_created[10][20][64],
			vid_pkt_destroyed[10][20][64],
			data_pkt_created[10][20][64],
			data_pkt_destroyed[10][20][64];
	int		loadOrderCounter,
			runNum;
	
} sIndicators;

// Declare Global Test Variables
sIndicators test_vars;
FILE	*indicatorFile;

#ifdef	EnableTroubleshooting_v2
FILE	*TSstream;
#endif

#ifdef	EnableTroubleshooting_v3
FILE	*status_processes_temp1;
#endif

#ifdef	EnableTroubleshooting_v4
FILE	*ONU_files[32];
#endif

FILE	*droppedScalPackets;

#define DATA_QUEUE_MAX_LENGTH 	400000
#define VIDEO_QUEUE_MAX_LENGTH 	400000

// Temporarily hard-code the moving average window size
#define Length_overallVideoQueueDelay_MovingAverage		5
#define LowerBound_scalableDropping		0.0005
#define UpperBound_scalableDropping		0.003

// Declare Troubleshooting Function Prototypes
void test_var_print(void);
void test_var_init(void);
void status_processes_print(void);
int file_exists(const char*);
void find_num_layers();
void find_num_frames();
void trace_on(void);
void trace_off(void);
void set_trace_file(FILE* f);
void set_output_file(FILE* f);
void status_processes(void);
int TSprint(const char*, ...);
int ONUprint(int, const char*, ...);

/*----------------End David's Troubleshooting----------------*/

#endif



