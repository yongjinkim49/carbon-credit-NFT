pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract AdvancedCollectible is ERC721, VRFConsumerBase {
    uint256 public tokenCounter;
    enum TypeOfAsset{AVOIDED_CONVERSION, REFORESTATION, AFORESTATION, LAND_CONSERVATION}
    enum Geolocation{CHINA, FRANCE, SOUTH_KOREA, INDIA, LEBANON}
    enum Soil{GRASS, MANGROVE, DESERT}
    enum Trees{SEQUOIA, ACACIAS, JUNGLE_TREES, KAPOK, BRAZIL_NUT, CECROPIA, ANNATTO, CHEWING_GUM_TREE}
    enum FloodRisk{LOW, MEDIUM, HIGH}
    enum FireRisk{LOW, MEDIUM, HIGH}
    enum DroughtRisk{LOW, MEDIUM, HIGH}
    // add other things
    mapping(bytes32 => address) public requestIdToSender;
    mapping(bytes32 => string) public requestIdToTokenURI;
    mapping(uint256 => TypeOfAsset) public tokenIdToTypeOfAsset;
    mapping(uint256 => Geolocation) public tokenIdToGeolocation;
    mapping(uint256 => Soil) public tokenIdToSoil;
    mapping(uint256 => Trees) public tokenIdToTrees;
    mapping(uint256 => FloodRisk) public tokenIdToFloodRisk;
    mapping(uint256 => FireRisk) public tokenIdToFireRisk;
    mapping(uint256 => DroughtRisk) public tokenIdToDroughtRisk;
    mapping(bytes32 => uint256) public requestIdToTokenId;
    event RequestedCollectible(bytes32 indexed requestId); 
    event ReturnedCollectible(bytes32 indexed requestId, uint256 randomNumber);


    bytes32 internal keyHash;
    uint256 internal fee;
    
    constructor(address _VRFCoordinator, address _LinkToken, bytes32 _keyhash)
    public 
    VRFConsumerBase(_VRFCoordinator, _LinkToken)
    ERC721("CarbonCaptureProjects", "C-BLOCK")
    {
        tokenCounter = 0;
        keyHash = _keyhash;
        fee = 0.1 * 10 ** 18;
    }

    function createCollectible(string memory tokenURI) 
        public returns (bytes32){
            bytes32 requestId = requestRandomness(keyHash, fee);
            requestIdToSender[requestId] = msg.sender;
            requestIdToTokenURI[requestId] = tokenURI;
            emit RequestedCollectible(requestId);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber) internal override {
        address landOwner = requestIdToSender[requestId];
        string memory tokenURI = requestIdToTokenURI[requestId];
        uint256 newItemId = tokenCounter;
        _safeMint(landOwner, newItemId);
        _setTokenURI(newItemId, tokenURI);
        
        TypeOfAsset typeofasset = TypeOfAsset(randomNumber % 4); 
        tokenIdToTypeOfAsset[newItemId] = typeofasset;

        Geolocation geolocation = Geolocation(randomNumber % 5); 
        tokenIdToGeolocation[newItemId] = geolocation;

        Soil soil = Soil(randomNumber % 3); 
        tokenIdToSoil[newItemId] = soil;

        Trees trees = Trees(randomNumber % 8); 
        tokenIdToTrees[newItemId] = trees;

        FloodRisk floodrisk = FloodRisk(randomNumber % 3); 
        tokenIdToFloodRisk[newItemId] = floodrisk;
        
        FireRisk firerisk = FireRisk(randomNumber % 3); 
        tokenIdToFireRisk[newItemId] = firerisk;

        DroughtRisk droughtrisk = DroughtRisk(randomNumber % 3); 
        tokenIdToDroughtRisk[newItemId] = droughtrisk;

        requestIdToTokenId[requestId] = newItemId;
        tokenCounter = tokenCounter + 1;
        emit ReturnedCollectible(requestId, randomNumber);
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: transfer caller is not owner nor approved"
        );
        _setTokenURI(tokenId, _tokenURI);
    }
}
